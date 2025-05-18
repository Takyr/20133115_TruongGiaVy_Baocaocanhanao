from puzzle import Puzzle
import pygame
import pygame_gui
import time
import colors

SCREEN_SIZE = (1280, 720)

#Setup
pygame.init()
BASICFONT = pygame.font.Font('ARIBLK.ttf',50)

pygame.display.set_caption('20133115_TruongGiaVy_8puzzle')
window_surface = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.Surface(SCREEN_SIZE)
background.fill(pygame.Color(colors.BABY_BLUE))
manager = pygame_gui.UIManager(SCREEN_SIZE, 'theme.json')

programIcon = pygame.image.load('logo.png')
pygame.display.set_icon(programIcon)

pygame_gui.core.IWindowInterface.set_display_title(self=window_surface,new_title="8-Puzzle")


#Tiêu đề
def display_elements():

    pygame_gui.elements.ui_label.UILabel(manager=manager,
                                        text="8-Puzzle Game",
                                        relative_rect=pygame.Rect((540, 10), (300, 70)),
                                        object_id="#title_box"
                                        )
    


display_elements()

# Nút giải thuật toán
solve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 640), (250, 45)),
                                             text='Giải Puzzle',
                                             manager=manager,
                                             object_id="#solve_btn")

#Danh sách thuật toán
dropdown_layout_rect = pygame.Rect((970, 600), (280, 35))
algorithmOptions = ["A* (Khoảng cách Manhatan)","Best-First (Khoảng cách Manhatan)"]
algorithmDropDown = pygame_gui.elements.UIDropDownMenu(options_list=algorithmOptions,
                                                       starting_option=algorithmOptions[1],
                                                       relative_rect=dropdown_layout_rect,
                                                       manager=manager)

#Các Label tìm kiếm
pygame_gui.elements.ui_label.UILabel(parent_element=algorithmDropDown,
                                     manager=manager,
                                     text="Heuristic Search:", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((800, 600), (170, 30)))


report_rect = pygame.Rect((1000, 210), (250, 30))
Final_state = pygame_gui.elements.UITextEntryLine(relative_rect=report_rect,
                                                  manager=manager)



pygame_gui.elements.ui_label.UILabel(parent_element=Final_state,
                                     manager=manager,
                                     text="Final:", # (pos-width,pos-height),(width,height)
                                     relative_rect=pygame.Rect((855, 210), (140, 30)))

### Cài đặt tình trạng Final
set_final_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 250), (250, 30)),
                                                text='Cài đặt Final',
                                                manager=manager)
### Nút xáo trộn thứ tự
button_layout_rect = pygame.Rect((1000, 290), (250, 30))
shuffle_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='Đảo',
                                             manager=manager)

info_html = "<b>C<b>!!!"
button_layout_rect = pygame.Rect((1250, 690), (30, 30))
info_button = pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                             text='?',
                                             manager=manager,
                                             tool_tip_text=info_html)

alert_label = pygame_gui.elements.ui_label.UILabel(
                                     manager=manager,
                                     text="",
                                     relative_rect=pygame.Rect((920, 320), (250, 30)),
                                     object_id="#accept_label")


def draw_blocks(blocks):
    for block in blocks:
        if block['block'] != 0:
            pygame.draw.rect(window_surface, colors.BLUE_GROTTO, block['rect'])
            textSurf = BASICFONT.render(str(block['block']), True, colors.NAVY_BLUE)
            textRect = textSurf.get_rect()
            textRect.center = block['rect'].left+50,block['rect'].top+50
            window_surface.blit(textSurf, textRect)
        else:
            pygame.draw.rect(window_surface, colors.ROYAL_BLUE, block['rect'])

def solveAnimation(moves):
    for mv in moves:
        zero = puzzle.matrix.searchBlock(0)
        if mv == "right":
            puzzle.matrix.moveright(zero)
        elif mv == "left":
            puzzle.matrix.moveleft(zero)  
        elif mv == "up":
            puzzle.matrix.moveup(zero)
        elif mv == "down":
            puzzle.matrix.movedown(zero)
        puzzle.setBlocksMatrix()
        draw_blocks(puzzle.blocks)
        pygame.display.update()
        time.sleep(0.2)
        
window_surface.blit(background, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
puzzle = Puzzle.new(250, 220, 330, 330)
puzzle.initialize()
algorithm = "Best-First (Khoảng cách Manhatan)"
fstate="1,2,3,4,5,6,7,8,0"
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == shuffle_button:
                    puzzle.randomBlocks()
                elif event.ui_element == set_final_button:
                    if not puzzle.setBlocks(Final_state.get_text()):
                        alert_label.set_text("!")
                    else:
                        alert_label.set_text("!")
                        puzzle.final_state = Final_state.get_text()
                elif event.ui_element == info_button:
                    Info_msg = '<b>8 Puzzle<br><br>Tác giả:</b><br><br>'
                   
                    info_win = pygame_gui.windows.ui_confirmation_dialog.UIConfirmationDialog(rect = pygame.Rect((600, 300), (180, 80)),
                                                                                            manager = manager,
                                                                                            action_long_desc = Info_msg,
                                                                                            window_title ='Developers Info',
                                                                                            )
                elif event.ui_element == solve_button:
                    
                    if algorithm == "Best-First (Khoảng cách Manhatan)":
                        moves = puzzle.bestFirst()
                        tempo = "{temp: .5f} giây".format(temp = puzzle.lastSolveTime)
                        report_msg = '<b>Các nút:</b> '+str(puzzle.cost)+'        <b>Thời gian:</b>'+tempo+ '        <b>Giải trong:</b> '+str(len(moves))+' bước'
                        # Báo cáo kết quả BFS
                        confirmation_win = pygame_gui.windows.ui_confirmation_dialog.UIConfirmationDialog(rect = pygame.Rect((600, 300), (180, 80)),
                                                                                                manager = manager,
                                                                                                action_long_desc = report_msg,
                                                                                                window_title =algorithm.split(" ")[0] + ' Báo cáo',
                                                                                                )
                        solveAnimation(moves)
                        
                    elif algorithm == "A* (Khoảng cách Manhatan)":
                        moves = puzzle.a_star()
                        tempo = "{temp: .5f} giây".format(temp = puzzle.lastSolveTime)
                        report_msg = '<b>Các nút:</b> '+str(puzzle.cost)+'        <b>Thời gian:</b>'+tempo+ '        <b>Giải trong:</b> '+str(len(moves))+' bước'
                        # Báo cáo kết quả A*
                        confirmation_win = pygame_gui.windows.ui_confirmation_dialog.UIConfirmationDialog(rect = pygame.Rect((600, 300), (180, 80)),
                                                                                                manager = manager,
                                                                                                action_long_desc = report_msg,
                                                                                                window_title =algorithm.split(" ")[0] + ' Báo cáo',
                                                                                                )
                        solveAnimation(moves)
                        
            elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == algorithmDropDown:
                    algorithm = event.text
            elif event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_element == Final_state:
                print("")
        manager.process_events(event)
        
        
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    draw_blocks(puzzle.blocks)
    pygame.display.update()
