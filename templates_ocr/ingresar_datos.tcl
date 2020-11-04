#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Nov 03, 2020 07:15:38 PM EST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 985x568+134+84
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 729
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Ocr Factura"
    vTcl:DefineAlias "$top" "ventana" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    $top.m45 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label {Ingresar Datos} 
    $top.m45 add command \
        -activebackground {} -activeforeground {} -background {} -command {#} \
        -font {} -foreground {} -label {Realizar Consultas} 
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background #f4f4f2 -height 565 \
        -width 954 
    vTcl:DefineAlias "$top.fra46" "contenedor" vTcl:WidgetProc "ventana" 1
    set site_3_0 $top.fra46
    button $site_3_0.but47 \
        -activebackground #bbbfca -activeforeground #495464 \
        -background #495464 -borderwidth 0 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #e8e8e8 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text Seleccionar 
    vTcl:DefineAlias "$site_3_0.but47" "btn_seleccionar" vTcl:WidgetProc "ventana" 1
    label $site_3_0.lab48 \
        -background #e8e8e8 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 10 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Ningun archivo} 
    vTcl:DefineAlias "$site_3_0.lab48" "lb_archivo" vTcl:WidgetProc "ventana" 1
    label $site_3_0.lab49 \
        -background #ff0000 -borderwidth 0 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) 
    vTcl:DefineAlias "$site_3_0.lab49" "lb_estado" vTcl:WidgetProc "ventana" 1
    label $site_3_0.lab50 \
        -background #f4f4f2 -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -text {No se ha cargado ningun archivo} 
    vTcl:DefineAlias "$site_3_0.lab50" "lb_mensaje_estado" vTcl:WidgetProc "ventana" 1
    button $site_3_0.but51 \
        -activebackground #bbbfca -activeforeground #495464 \
        -background #495464 -borderwidth 0 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #e8e8e8 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text Analizar 
    vTcl:DefineAlias "$site_3_0.but51" "btn_analizar" vTcl:WidgetProc "ventana" 1
    button $site_3_0.but53 \
        -activebackground #bbbfca -activeforeground #495464 \
        -background #495464 -borderwidth 0 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #e8e8e8 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text {Guardar Dato(s)} 
    vTcl:DefineAlias "$site_3_0.but53" "btn_guardar" vTcl:WidgetProc "ventana" 1
    vTcl::widgets::ttk::scrolledwindow::CreateCmd $site_3_0.scr57 \
        -borderwidth 2 -background $vTcl(actual_gui_bg) -height 437 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 932 
    vTcl:DefineAlias "$site_3_0.scr57" "scroll" vTcl:WidgetProc "ventana" 1

    $site_3_0.scr57.01 configure -background white \
        -borderwidth 2 \
        -height 75 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -relief groove \
        -selectbackground blue \
        -selectforeground white \
        -width 125
    ttk::entry $site_3_0.scr57.01.tEn58 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn58" "TEntry1" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn60 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn60" "TEntry1_1" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn61 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn61" "TEntry1_2" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn62 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn62" "TEntry1_3" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn63 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn63" "TEntry1_4" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn64 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn64" "TEntry1_5" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn65 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn65" "TEntry1_6" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn66 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn66" "TEntry1_7" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn67 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn67" "TEntry1_8" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn68 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn68" "TEntry1_9" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn69 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn69" "TEntry1_10" vTcl:WidgetProc "ventana" 1
    ttk::entry $site_3_0.scr57.01.tEn70 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$site_3_0.scr57.01.tEn70" "TEntry1_11" vTcl:WidgetProc "ventana" 1
    place $site_3_0.scr57.01.tEn58 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.003 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn60 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.085 -y 0 -rely 0.023 -width 78 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn61 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.169 -y 0 -rely 0.023 -width 78 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn62 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.254 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn63 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.338 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn64 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.423 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn65 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.507 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn66 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.592 -y 0 -rely 0.023 -width 78 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn67 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.676 -y 0 -rely 0.023 -width 78 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn68 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.761 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn69 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.93 -y 0 -rely 0.023 -width 77 \
        -relwidth 0 -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57.01.tEn70 \
        -in $site_3_0.scr57.01 -x 0 -relx 0.845 -y 0 -rely 0.023 -width 0 \
        -relwidth 0.085 -height 0 -relheight 0.046 -anchor nw \
        -bordermode ignore 
    ttk::progressbar $site_3_0.tPr71 \
        -length 980 
    vTcl:DefineAlias "$site_3_0.tPr71" "pb_progreso" vTcl:WidgetProc "ventana" 1
    place $site_3_0.but47 \
        -in $site_3_0 -x 0 -relx 0.01 -y 0 -rely 0.018 -width 160 -relwidth 0 \
        -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.178 -y 0 -rely 0.018 -width 0 \
        -relwidth 0.304 -height 0 -relheight 0.062 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.493 -y 0 -rely 0.018 -width 0 \
        -relwidth 0.039 -height 0 -relheight 0.062 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.545 -y 0 -rely 0.018 -width 0 \
        -relwidth 0.202 -height 0 -relheight 0.062 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.797 -y 0 -rely 0.018 -width 180 \
        -relwidth 0 -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -relx 0.797 -y 0 -rely 0.885 -width 180 \
        -relwidth 0 -height 35 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.scr57 \
        -in $site_3_0 -x 0 -relx 0.01 -y 0 -rely 0.106 -width 0 \
        -relwidth 0.977 -height 0 -relheight 0.772 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tPr71 \
        -in $site_3_0 -x 0 -y 0 -rely 0.956 -width 0 -relwidth 0.999 \
        -height 22 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 0.996 -height 0 \
        -relheight 0.995 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

