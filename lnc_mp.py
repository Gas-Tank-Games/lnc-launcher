import pygame
import gamejoltapi
import subprocess
import os

pygame.init()
pygame.mixer.init()
pygame.display.set_icon(pygame.image.load('launcher_files/icon.ico'))

WIDTH, HEIGHT = 1000, 800
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life n' Crime Online")

# Assets
tile_image = pygame.image.load("launcher_files/mp/bg.png").convert()
logo_image = pygame.image.load("launcher_files/mp/logo.png").convert_alpha()
mode_image = pygame.image.load("launcher_files/mp/mode.png").convert_alpha()
button_image = pygame.image.load("launcher_files/mp/button.png").convert_alpha()
click_sound = pygame.mixer.Sound("launcher_files/mp/punch.mp3")
button_font = pygame.font.SysFont("Comic Sans MS", 26)
button_font_small = pygame.font.SysFont("Comic Sans MS", 16)
rus_button_image = pygame.image.load("launcher_files/mp/rus_button.png").convert_alpha()

playernum = 2
playernum_limit = 6
netmode = 0
netmodetext = "Netmode: P2P"
mode = ""

class Button:
    def __init__(self, rect, text, callback, font, image, click_sound):
        self.rect = pygame.Rect(rect)
        self.font = font
        self.text_surface = self.font.render(text, True, (0, 0, 0))
        self.callback = callback
        self.click_sound = click_sound
        self.image = pygame.transform.scale(image, (self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(self.image)
        self.hovered = False
    def update(self, mouse_pos):
        rel_x = mouse_pos[0] - self.rect.x
        rel_y = mouse_pos[1] - self.rect.y
        self.hovered = (0 <= rel_x < self.rect.width and 0 <= rel_y < self.rect.height and self.mask.get_at((int(rel_x), int(rel_y))))
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.hovered:
            self.draw_outline(surface)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        surface.blit(self.text_surface, text_rect)
    def draw_outline(self, surface):
        outline_points = self.mask.outline()
        for point in outline_points:
            surface.set_at((point[0] + self.rect.x, point[1] + self.rect.y), BLACK)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.click_sound.play()
            self.callback()

class InputField:
    def __init__(self, rect, default_if_text, font, is_password=False, text_color=(0, 0, 0), bg_color=(255, 255, 255), border_color=(0, 0, 0), max_length=20):
        self.rect = pygame.Rect(rect)
        self.font = font
        self.text = default_if_text
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.active = False
        self.max_length = max_length
        self.cursor_visible = True
        self.cursor_counter = 0
        self.is_password = is_password
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                self.active = False
            elif len(self.text) < self.max_length and event.unicode.isprintable():
                self.text += event.unicode
    def update(self):
        if self.active:
            self.cursor_counter += 1
            if self.cursor_counter >= 30:
                self.cursor_counter = 0
                self.cursor_visible = not self.cursor_visible
        else:
            self.cursor_visible = False
    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        display_text = '*' * len(self.text) if self.is_password else self.text
        if self.active and self.cursor_visible:
            display_text += "|"
        text_surf = self.font.render(display_text, True, self.text_color)
        surface.blit(text_surf, (self.rect.x + 5, self.rect.y + (self.rect.height - text_surf.get_height()) // 2))
    def get_text(self):
        return self.text
    def clear(self):
        self.text = ""

class Page:
    def __init__(self):
        self.buttons = []
    def enter(self):
        pass
    def exit(self):
        pass
    def update(self, mouse_pos):
        for btn in self.buttons:
            btn.update(mouse_pos)
    def draw(self, surface):
        for btn in self.buttons:
            btn.draw(surface)
    def handle_event(self, event):
        for btn in self.buttons:
            btn.handle_event(event)

class PageManager:
    def __init__(self):
        self.current_page = None
    def set_page(self, page):
        if self.current_page:
            self.current_page.exit()
        self.current_page = page
        self.current_page.enter()
    def update(self, mouse_pos):
        if self.current_page:
            self.current_page.update(mouse_pos)
    def draw(self, surface):
        if self.current_page:
            self.current_page.draw(surface)
    def handle_event(self, event):
        if self.current_page:
            self.current_page.handle_event(event)

class MainMenuPage(Page):
    def enter(self):
        self.buttons = [
            Button(pygame.Rect(400, 500, 200, 60), "Host", lambda: page_manager.set_page(mode_page), button_font, button_image, click_sound),
            Button(pygame.Rect(400, 600, 200, 60), "Join", lambda: page_manager.set_page(join_page), button_font, button_image, click_sound),
        ]

    def draw(self, surface):
        tile_width, tile_height = tile_image.get_width(), tile_image.get_height()
        for x in range(0, WIDTH, tile_width):
            for y in range(0, HEIGHT, tile_height):
                surface.blit(tile_image, (x, y))
        logo_rect = logo_image.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        surface.blit(logo_image, logo_rect)
        super().draw(surface)

class GJErrorPage(Page):
    def enter(self):
        self.buttons = []
    def draw(self, surface):
        tile_width, tile_height = tile_image.get_width(), tile_image.get_height()
        for x in range(0, WIDTH, tile_width):
            for y in range(0, HEIGHT, tile_height):
                surface.blit(tile_image, (x, y))
        logo_rect = logo_image.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        surface.blit(logo_image, logo_rect)
        gjerror_label = button_font.render("Please connect your GameJolt Account in the Launcher to play LNC ONLINE!", True, (230, 0, 0))
        errorinfo_label = button_font_small.render("(This is so we can save and track your progress, we are not affiliated with Gamejolt!)", True, (255, 255, 255))
        surface.blit(gjerror_label, (40, 500))
        surface.blit(errorinfo_label, (200, 540))
        super().draw(surface)
        
class ModeSelectPage(Page):
    def enter(self):
        self.buttons = [
            Button(pygame.Rect(400, 300, 200, 200), "", lambda: self.select_mode("Russian Roulette", 6), button_font, rus_button_image, click_sound),
            Button(pygame.Rect(400, 700, 200, 60), "Main Menu", lambda: page_manager.set_page(main_menu_page), button_font, button_image, click_sound)
        ]

    def draw(self, surface):
        tile_width, tile_height = tile_image.get_width(), tile_image.get_height()
        for x in range(0, WIDTH, tile_width):
            for y in range(0, HEIGHT, tile_height):
                surface.blit(tile_image, (x, y))
        mode_rect = mode_image.get_rect(center=(WIDTH // 2, 100))
        surface.blit(mode_image, mode_rect)
        super().draw(surface)
    def select_mode(self, selected_mode, limit):
        global mode, playernum, playernum_limit
        mode = selected_mode
        playernum_limit = limit
        playernum = 2
        if mode == "Russian Roulette":
            page_manager.set_page(rus_host_page)

class RusHostPage(Page):
    def enter(self):
        self.port_field = InputField(pygame.Rect(350, 435, 300, 50), "5029", button_font)
        self.buttons = [
            Button(pygame.Rect(200, 250, 200, 60), "<", self.lower_player, button_font, button_image, click_sound),
            Button(pygame.Rect(600, 250, 200, 60), ">", self.higher_player, button_font, button_image, click_sound),
            #Button(pygame.Rect(600, 400, 200, 60), netmodetext, self.toggle_netmode, button_font, button_image, click_sound),
            Button(pygame.Rect(400, 600, 200, 60), "Host", lambda: self.host, button_font, button_image, click_sound),
            Button(pygame.Rect(400, 700, 200, 60), "Main Menu", lambda: page_manager.set_page(main_menu_page), button_font, button_image, click_sound),
        ]
    def handle_event(self, event):
        super().handle_event(event)
        self.port_field.handle_event(event)
    def draw(self, surface):
        tile_width, tile_height = tile_image.get_width(), tile_image.get_height()
        for x in range(0, WIDTH, tile_width):
            for y in range(0, HEIGHT, tile_height):
                surface.blit(tile_image, (x, y))
        number_text = button_font.render(str(playernum), True, (255, 255, 255))    
        surface.blit(number_text, (495, 260))
        super().draw(surface)
        port_label = button_font.render("Port:", True, (255, 255, 255))
        number_label = button_font.render("Number of Players:", True, (255, 255, 255))
        surface.blit(port_label, (470, 360))
        surface.blit(number_label, (400, 180))
        self.port_field.draw(surface)
    def update(self, mouse_pos):
        super().update(mouse_pos)
        self.port_field.update()
    def lower_player(self):
        global playernum
        if playernum > 2:
            playernum -= 1
    def higher_player(self):
        global playernum
        if playernum < playernum_limit:
            playernum += 1
    def host(self):
        global playernum
        subprocess.run("start files/lnc.exe -iwad gamefiles.ipk3 -is_launcher_launched -gamejolt -host " + str(playernum) + " -deathmatch -port " + str(self.port_field.get_text()) + " +map rus01 +multiplayer_current_mode 3 +r_deathcamera true +sv_noautomap true +sv_nocrouch true +sv_nojump true" if os.name == "nt" else "", shell=True)
    #def toggle_netmode (self): 
    #    global netmode
    #    global netmodetext
    #    if netmode == 0:
    #        netmode = 1
    #        netmodetext = "Netmode: Packet Server"
    #    if netmode == 1:
    #        netmode = 0
    #        netmodetext = "Netmode: P2P"

class JoinPage(Page):
    def enter(self):
        self.join_adr_field = InputField(pygame.Rect(350, 300, 300, 50), "", button_font, is_password=True)
        self.buttons = [
            Button(pygame.Rect(400, 600, 200, 60), "Join", lambda: self.join, button_font, button_image, click_sound),
            Button(pygame.Rect(400, 700, 200, 60), "Main Menu", lambda: page_manager.set_page(main_menu_page), button_font, button_image, click_sound),
        ]
    def handle_event(self, event):
        super().handle_event(event)
        self.join_adr_field.handle_event(event)
    def update(self, mouse_pos):
        super().update(mouse_pos)
        self.join_adr_field.update()
    def draw(self, surface):
        tile_width, tile_height = tile_image.get_width(), tile_image.get_height()
        for x in range(0, WIDTH, tile_width):
            for y in range(0, HEIGHT, tile_height):
                surface.blit(tile_image, (x, y))
        super().draw(surface)
        self.join_adr_field.draw(surface)
        ip_label = button_font.render("LAN/WAN Adress:", True, (255, 255, 255))
        surface.blit(ip_label, (390, 210))
    def join(self):
        subprocess.run("start files/lnc.exe -iwad gamefiles.ipk3 -is_launcher_launched -gamejolt -join " + str(self.join_adr_field.get_text()) if os.name == "nt" else "", shell=True)

page_manager = PageManager()
main_menu_page = MainMenuPage()
mode_page = ModeSelectPage()
gamejolt_error_page = GJErrorPage()
rus_host_page = RusHostPage()
join_page = JoinPage()
if os.path.exists("lnc_gj_credts"):
    page_manager.set_page(main_menu_page)
else:
    page_manager.set_page(gamejolt_error_page)
clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        page_manager.handle_event(event)
    page_manager.update(mouse_pos)
    screen.fill(BLACK)
    page_manager.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()