import pyautogui
import time

time.sleep(5)  # Asteapta 5 secunde pana la cautarea primei imagini

refresh = 'refresh.png'             
people = 'people.png'               
see_all = 'see-all.png'             
oops_ok = 'oops-ok.png'             

# user 1
image_path_1 = 'imagine1.png'       
image_path_2 = 'imagine2.png'       
image_path_3 = 'imagine3.png'       
image_path_4 = 'imagine4.png'       
image_path_5 = 'imagine5.png'       

#user 2
image_path_6 = 'imagine1.png'
image_path_7 = 'imagine2.png'
image_path_8 = 'imagine3.png'
image_path_9 = 'imagine4.png'
image_path_10 = 'imagine5.png'

#user 3
image_path_11 = 'imagine1.png'
image_path_12 = 'imagine2.png'
image_path_13 = 'imagine3.png'
image_path_14 = 'imagine4.png'
image_path_15 = 'imagine5.png'

# user 4
image_path_16 = 'imagine1.png'
image_path_17 = 'imagine2.png'
image_path_18 = 'imagine3.png'
image_path_19 = 'imagine4.png'
image_path_20 = 'imagine5.png'

# user 5
image_path_21 = 'imagine1.png'
image_path_22 = 'imagine2.png'
image_path_23 = 'imagine3.png'
image_path_24 = 'imagine4.png'
image_path_25 = 'imagine5.png'

# user 6
image_path_26 = 'imagine1.png'
image_path_27 = 'imagine2.png'
image_path_28 = 'imagine3.png'
image_path_29 = 'imagine4.png'
image_path_30 = 'imagine5.png'

# user 7
image_path_31 = 'imagine1.png'
image_path_32 = 'imagine2.png'
image_path_33 = 'imagine3.png'
image_path_34 = 'imagine4.png'
image_path_35 = 'imagine5.png'

# Cauta imaginea pe ecran
while True:
    location_people = pyautogui.locateOnScreen(people, confidence=0.8)
    if location_people:
        center_people = pyautogui.center(location_people)
        print(f'Imaginea people a fost gasita la {center_people}.')
        
        offset_x = 0  
        offset_y = 0
        click_x = center_people.x + offset_x  
        click_y = center_people.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe people la ({click_x}, {click_y}).')
        time.sleep(2)  

        pyautogui.scroll(-600)  
        print('Scroll in jos 600')

        time.sleep(2) 

    location_see_all = pyautogui.locateOnScreen(see_all, confidence=0.8)
    if location_see_all:
        center_see_all = pyautogui.center(location_see_all)
        print(f'Imaginea see_all a fost gasita la {center_see_all}.')
        
        offset_x = 0  
        offset_y = 0
        click_x = center_see_all.x + offset_x  
        click_y = center_see_all.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe see_all la ({click_x}, {click_y}).')
        time.sleep(2)  

        pyautogui.scroll(-1200)  
        print('Scroll in jos 1200')
        time.sleep(2)

        pyautogui.scroll(-60)  
        print('Scroll in jos 60')
        time.sleep(2)
    
    # Cauta prima imagine
    location_1 = pyautogui.locateOnScreen(image_path_1, confidence=0.4)
    if location_1:
        center_1 = pyautogui.center(location_1)
        print(f'Imaginea image_path_1 a fost gasita la {center_1}.')
        
        offset_x = 0  
        offset_y = -250
        click_x = center_1.x + offset_x  
        click_y = center_1.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_1 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_1 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_2 = pyautogui.locateOnScreen(image_path_2, confidence=0.8)
    if location_2:
        center_2 = pyautogui.center(location_2)
        pyautogui.click(center_2)
        print(f'Click pe image_path_2 la {center_2}.')
        time.sleep(2)
    else:
        print(f'image_path_2 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_3 = pyautogui.locateOnScreen(image_path_3, confidence=0.6)
        if location_3:
            center_3 = pyautogui.center(location_3)
            
            offset_x = 500  
            click_x = center_3.x + offset_x  
            click_y = center_3.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_3 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_3} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_3} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_4 = pyautogui.locateOnScreen(image_path_4, confidence=0.4)
        if location_4:
            center_4 = pyautogui.center(location_4)
            print(f'Imaginea image_path_4 a fost gasita la {center_4}.')
            
            offset_x = 500  
            click_x = center_4.x + offset_x  
            click_y = center_4.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_4 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_4} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_4} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_5 = pyautogui.locateOnScreen(image_path_5, confidence=0.8)
    if location_5:
        center_5 = pyautogui.center(location_5)
        pyautogui.click(center_5)
        print(f'Click pe image_path_5 la {center_5}.')
        time.sleep(2)
    else:
        print(f'image_path_5 nu a fost gasita pe ecran.')

    time.sleep(2)

    try:
        location_oops_ok = pyautogui.locateOnScreen(oops_ok, confidence=0.8)
        if location_oops_ok:
            center_oops_ok = pyautogui.center(location_oops_ok)
            pyautogui.click(center_oops_ok)
            print(f'Click pe oops_ok la {center_oops_ok}.')
            time.sleep(2)
        else:
            print('oops_ok nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print('oops_ok nu a fost gasita pe ecran.')

    time.sleep(2)

    #reia
    location_6 = pyautogui.locateOnScreen(image_path_6, confidence=0.4)
    if location_6:
        center_6 = pyautogui.center(location_6)
        print(f'Imaginea image_path_6 a fost gasita la {center_6}.')
        
        offset_x = 0  
        offset_y = -140
        click_x = center_6.x + offset_x  
        click_y = center_6.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_6 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_6 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_7 = pyautogui.locateOnScreen(image_path_7, confidence=0.8)
    if location_7:
        center_7 = pyautogui.center(location_7)
        pyautogui.click(center_7)
        print(f'Click pe image_path_7 la {center_7}.')
        time.sleep(2)
    else:
        print(f'image_path_7 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_8 = pyautogui.locateOnScreen(image_path_8, confidence=0.6)
        if location_8:
            center_8 = pyautogui.center(location_8)
            
            offset_x = 500  
            click_x = center_8.x + offset_x  
            click_y = center_8.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_8 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_8} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_8} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_9 = pyautogui.locateOnScreen(image_path_9, confidence=0.4)
        if location_9:
            center_9 = pyautogui.center(location_9)
            print(f'Imaginea image_path_9 a fost gasita la {center_9}.')
            
            offset_x = 500  
            click_x = center_9.x + offset_x  
            click_y = center_9.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_9 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_9} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_9} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_10 = pyautogui.locateOnScreen(image_path_10, confidence=0.8)
    if location_10:
        center_10 = pyautogui.center(location_10)
        pyautogui.click(center_10)
        print(f'Click pe image_path_10 la {center_10}.')
        time.sleep(2)
    else:
        print(f'image_path_10 nu a fost gasita pe ecran.')

    time.sleep(2)

    try:
        location_oops_ok = pyautogui.locateOnScreen(oops_ok, confidence=0.8)
        if location_oops_ok:
            center_oops_ok = pyautogui.center(location_oops_ok)
            pyautogui.click(center_oops_ok)
            print(f'Click pe oops_ok la {center_oops_ok}.')
            time.sleep(2)
        else:
            print('oops_ok nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print('oops_ok nu a fost gasita pe ecran.')

    time.sleep(2)
    
    #reia
    location_11 = pyautogui.locateOnScreen(image_path_11, confidence=0.4)
    if location_11:
        center_11 = pyautogui.center(location_11)
        print(f'Imaginea image_path_11 a fost gasita la {center_11}.')
        
        offset_x = 0  
        offset_y = 0
        click_x = center_11.x + offset_x  
        click_y = center_11.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_11 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_11 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_12 = pyautogui.locateOnScreen(image_path_12, confidence=0.8)
    if location_12:
        center_12 = pyautogui.center(location_12)
        pyautogui.click(center_12)
        print(f'Click pe image_path_12 la {center_12}.')
        time.sleep(2)
    else:
        print(f'image_path_12 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_13 = pyautogui.locateOnScreen(image_path_13, confidence=0.6)
        if location_13:
            center_13 = pyautogui.center(location_13)
            
            offset_x = 500  
            click_x = center_13.x + offset_x  
            click_y = center_13.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_13 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_13} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_13} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_14 = pyautogui.locateOnScreen(image_path_14, confidence=0.4)
        if location_14:
            center_14 = pyautogui.center(location_14)
            print(f'Imaginea image_path_14 a fost gasita la {center_14}.')
            
            offset_x = 500  
            click_x = center_14.x + offset_x  
            click_y = center_14.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_14 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_14} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_14} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_15 = pyautogui.locateOnScreen(image_path_15, confidence=0.8)
    if location_15:
        center_15 = pyautogui.center(location_15)
        pyautogui.click(center_15)
        print(f'Click pe image_path_15 la {center_15}.')
        time.sleep(2)
    else:
        print(f'image_path_15 nu a fost gasita pe ecran.')

    time.sleep(2)

    try:
        location_oops_ok = pyautogui.locateOnScreen(oops_ok, confidence=0.8)
        if location_oops_ok:
            center_oops_ok = pyautogui.center(location_oops_ok)
            pyautogui.click(center_oops_ok)
            print(f'Click pe oops_ok la {center_oops_ok}.')
            time.sleep(2)
        else:
            print('oops_ok nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print('oops_ok nu a fost gasita pe ecran.')

    time.sleep(2)

    #reia
    location_16 = pyautogui.locateOnScreen(image_path_16, confidence=0.4)
    if location_16:
        center_16 = pyautogui.center(location_16)
        print(f'Imaginea image_path_16 a fost gasita la {center_16}.')
        
        offset_x = 0  
        offset_y = 100
        click_x = center_16.x + offset_x  
        click_y = center_16.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_16 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_16 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_17 = pyautogui.locateOnScreen(image_path_17, confidence=0.8)
    if location_17:
        center_17 = pyautogui.center(location_17)
        pyautogui.click(center_17)
        print(f'Click pe image_path_17 la {center_17}.')
        time.sleep(2)
    else:
        print(f'image_path_17 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_18 = pyautogui.locateOnScreen(image_path_18, confidence=0.6)
        if location_18:
            center_18 = pyautogui.center(location_18)
            
            offset_x = 500  
            click_x = center_18.x + offset_x  
            click_y = center_18.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_18 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_18} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_18} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_19 = pyautogui.locateOnScreen(image_path_19, confidence=0.4)
        if location_19:
            center_19 = pyautogui.center(location_19)
            print(f'Imaginea image_path_19 a fost gasita la {center_19}.')
            
            offset_x = 500  
            click_x = center_19.x + offset_x  
            click_y = center_19.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_19 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_19} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_19} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_20 = pyautogui.locateOnScreen(image_path_20, confidence=0.8)
    if location_20:
        center_20 = pyautogui.center(location_20)
        pyautogui.click(center_20)
        print(f'Click pe image_path_20 la {center_20}.')
        time.sleep(2)
    else:
        print(f'image_path_20 nu a fost gasita pe ecran.')

    time.sleep(2)

    try:
        location_oops_ok = pyautogui.locateOnScreen(oops_ok, confidence=0.8)
        if location_oops_ok:
            center_oops_ok = pyautogui.center(location_oops_ok)
            pyautogui.click(center_oops_ok)
            print(f'Click pe oops_ok la {center_oops_ok}.')
            time.sleep(2)
        else:
            print('oops_ok nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print('oops_ok nu a fost gasita pe ecran.')

    time.sleep(2)

    #reia
    location_21 = pyautogui.locateOnScreen(image_path_21, confidence=0.4)
    if location_21:
        center_21 = pyautogui.center(location_21)
        print(f'Imaginea image_path_21 a fost gasita la {center_21}.')
        
        offset_x = 0  
        offset_y = 200
        click_x = center_21.x + offset_x  
        click_y = center_21.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_21 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_21 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_22 = pyautogui.locateOnScreen(image_path_22, confidence=0.8)
    if location_22:
        center_22 = pyautogui.center(location_22)
        pyautogui.click(center_22)
        print(f'Click pe image_path_22 la {center_22}.')
        time.sleep(2)
    else:
        print(f'image_path_22 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_23 = pyautogui.locateOnScreen(image_path_23, confidence=0.6)
        if location_23:
            center_23 = pyautogui.center(location_23)
            
            offset_x = 500  
            click_x = center_23.x + offset_x  
            click_y = center_23.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_23 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_23} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_23} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_24 = pyautogui.locateOnScreen(image_path_24, confidence=0.4)
        if location_24:
            center_24 = pyautogui.center(location_24)
            print(f'Imaginea image_path_24 a fost gasita la {center_24}.')
            
            offset_x = 500  
            click_x = center_24.x + offset_x  
            click_y = center_24.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_24 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_24} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_24} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_25 = pyautogui.locateOnScreen(image_path_25, confidence=0.8)
    if location_25:
        center_25 = pyautogui.center(location_25)
        pyautogui.click(center_25)
        print(f'Click pe image_path_25 la {center_25}.')
        time.sleep(2)
    else:
        print(f'image_path_25 nu a fost gasita pe ecran.')

    time.sleep(2)

    #reia
    location_26 = pyautogui.locateOnScreen(image_path_26, confidence=0.448)
    if location_26:
        center_26 = pyautogui.center(location_26)
        print(f'Imaginea image_path_26 a fost gasita la {center_26}.')
        
        offset_x = 0  
        offset_y = 200
        click_x = center_26.x + offset_x  
        click_y = center_26.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_26 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_26 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_27 = pyautogui.locateOnScreen(image_path_27, confidence=0.8)
    if location_27:
        center_27 = pyautogui.center(location_27)
        pyautogui.click(center_27)
        print(f'Click pe image_path_27 la {center_27}.')
        time.sleep(2)
    else:
        print(f'image_path_27 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_28 = pyautogui.locateOnScreen(image_path_28, confidence=0.6)
        if location_28:
            center_29 = pyautogui.center(location_28)
            
            offset_x = 500  
            click_x = center_29.x + offset_x  
            click_y = center_29.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_28 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_28} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_28} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_29 = pyautogui.locateOnScreen(image_path_29, confidence=0.4)
        if location_29:
            center_29 = pyautogui.center(location_29)
            print(f'Imaginea image_path_29 a fost gasita la {center_29}.')
            
            offset_x = 500  
            click_x = center_29.x + offset_x  
            click_y = center_29.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_29 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_29} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_29} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_30 = pyautogui.locateOnScreen(image_path_30, confidence=0.8)
    if location_30:
        center_30 = pyautogui.center(location_30)
        pyautogui.click(center_30)
        print(f'Click pe image_path_30 la {center_30}.')
        time.sleep(2)
    else:
        print(f'image_path_30 nu a fost gasita pe ecran.')

    time.sleep(2)

    #reia
    location_31 = pyautogui.locateOnScreen(image_path_31, confidence=0.448)
    if location_31:
        center_31 = pyautogui.center(location_31)
        print(f'Imaginea image_path_31 a fost gasita la {center_31}.')
        
        offset_x = 0  
        offset_y = 310
        click_x = center_31.x + offset_x  
        click_y = center_31.y + offset_y  

        pyautogui.click(click_x, click_y)
        print(f'Click pe image_path_31 la ({click_x}, {click_y}).')
        time.sleep(2)  
    else:
        print(f'image_path_31 nu a fost gasita pe ecran.')

    # Cauta a doua imagine
    location_32 = pyautogui.locateOnScreen(image_path_32, confidence=0.8)
    if location_32:
        center_32 = pyautogui.center(location_32)
        pyautogui.click(center_32)
        print(f'Click pe image_path_32 la {center_32}.')
        time.sleep(2)
    else:
        print(f'image_path_32 nu a fost gasita pe ecran.')

    # Cauta a treia imagine
    try:
        location_33 = pyautogui.locateOnScreen(image_path_33, confidence=0.6)
        if location_33:
            center_33 = pyautogui.center(location_33)
            
            offset_x = 500  
            click_x = center_33.x + offset_x  
            click_y = center_33.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_33 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_33} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_33} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a patra imagine
    try:
        location_34 = pyautogui.locateOnScreen(image_path_34, confidence=0.4)
        if location_34:
            center_34 = pyautogui.center(location_34)
            print(f'Imaginea image_path_34 a fost gasita la {center_34}.')
            
            offset_x = 500  
            click_x = center_34.x + offset_x  
            click_y = center_34.y  

            pyautogui.click(click_x, click_y)
            print(f'Click pe image_path_34 la ({click_x}, {click_y}).')
            time.sleep(2)  
        else:
            print(f'{image_path_34} nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print(f'Eroare: {image_path_34} nu a fost gasita pe ecran.')

    time.sleep(2)

    # Cauta a cincea imagine
    location_35 = pyautogui.locateOnScreen(image_path_35, confidence=0.8)
    if location_35:
        center_35 = pyautogui.center(location_35)
        pyautogui.click(center_35)
        print(f'Click pe image_path_35 la {center_35}.')
        time.sleep(2)
    else:
        print(f'image_path_35 nu a fost gasita pe ecran.')

    time.sleep(2)

    try:
        location_oops_ok = pyautogui.locateOnScreen(oops_ok, confidence=0.8)
        if location_oops_ok:
            center_oops_ok = pyautogui.center(location_oops_ok)
            pyautogui.click(center_oops_ok)
            print(f'Click pe oops_ok la {center_oops_ok}.')
            time.sleep(2)
        else:
            print('oops_ok nu a fost gasita pe ecran.')
    except pyautogui.ImageNotFoundException:
        print('oops_ok nu a fost gasita pe ecran.')

    time.sleep(2)

    location_refresh = pyautogui.locateOnScreen(refresh, confidence=0.8)
    if location_refresh:
        center_refresh = pyautogui.center(location_refresh)
        print(f'Imaginea refresh a fost gasita la {center_refresh}.')
        
        pyautogui.click(center_refresh)
        print(f'Click pe refresh la ({center_refresh}).')
        
        time.sleep(5)  