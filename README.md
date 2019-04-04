# VHDL-Games
VHDL-Games consists of some simple realizations such as color bar, static picture and waves, as well as two games -- Retro Snaker and Tetris. 3 VHDL files and 4 Python files helping generate VHDL codes are included. Below is a description of them.
--./mode_1_to_6/bigbang.vhd
    This file contains mode 1 to mode 6, which show vertical color bar, horizontal color bar, checkerboard, static picture(Luna), analog and digital clocks and waves(triangular, square and sine), respectively. The code for the first two modes referenced [1]. The strategy of generating checkerboard can be concluded by noting the fact that the result of the xor of B-components of the first two color bars changes its values every other time. The code for the static pictures, words and clocks can be generated by Python files. Waves mode (mode 6) can show the three kinds of wave at 250*(1-8)kHz calculated by considering every pixel(200 used totally) as 1Hz of the system clock's frequency 50MHz. The waveforms can also be amplified and moved to the right in the X-axis direction, realized by modifying the part used in a waveform with only one complete cycle.
--./mode_7/bigbang.vhd
    In the mode 7, a player can play a game named Snake, i.e., the Retro Snaker. This game is realized mainly by two state matrices, state1[12][12] and state0[12][12]. There are 144 points in the main interface. The outermost circle is walls, corresponding to the state1[i][j]=1 and state0[i][j]=1 where i=0 or i=11 or j=0 or j=11. The snake, the food and the free space is corresponding to (state1[i][j],state0[i][j])=(0,1), (1,0) and (0,0), respectively. In addition, there are two arrays index_x[101] and index_y[101] recording the coordinates of the head and body of the snake. The coordinate of the head is always recorded at index_x[0] and index_y[0]. And the two index arrays are updated and modify the two state matrices every steps according to the direction, food, wall and its body, and then the VGA display displays different colors according to the state of a point.
--./mode_8/bigbang.vhd
    Mode 8 describes a Tetris game. Similar to the previous game, this game is realized using two state matrices which are modified by the state of a point and can control the color of a pixel of the VGA display.
--./py/vhdlGen.py
    This Python file generates the analog clock. The 'scal' is in order to eliminate the distortion due to the large difference between the number of horizontal and vertical pixels -- which are 479 and 251, respectively. The 'x0' and 'y0' is the coordinate of the centre of the analog clock, and the 'radius', the 'radius_hour', the 'radius_min' and the 'radius_sec' are the radius of the analog clock, the hour hand, the minute hand and the second hand.
--./py/vhdl_gen_dig.py
    This file can generate the VHDL code for characters according to the area and the color specified.
--./py/vhdl_gen_pic.py
    This file can generate the VHDL code for a static picture according to the original picture, the area and the color specified.
--./py/vhdl_gen_wave.py
    This file generates the table containing independent variables and sine function values used in the mode 6.

Environment and configuration:
Windows8.1
Quartus II 8.1
Anaconda3 + Spyder3.2.8
FPGA device: EP3C40Q240C8

References:
[1]潘松,王国栋.VHDL实用教程[M].电子科技大学出版社:成都,2001:316.
[2]李辉.VHDL与数字系统设计[M].中国科学技术大学出版社:合肥,2015:236. 
[3]wangyong_0306.基于FPGA的VGA显示详解(附VHDL代码)[EB/OL].https://wenku.baidu.com/view/688a8259ae45b307e87101f69e3143323868f50a.html,2018-08-07.

Note:
Since the FPGA device and the VGA display were supported by my university for the purpose of a course and I have finished it, I cannot improve my codes in the experiment any more. If conditions permit, I will continue to improve them.
