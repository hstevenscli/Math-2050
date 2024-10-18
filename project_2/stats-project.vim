let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/school/Math-2050/project_2
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +7 project.py
badd +94 HORMONE.csv
badd +0 hormone.txt
badd +0 pandas_df_operations.md
badd +995 term://~/school/Math-2050/project_2//121004:/bin/bash
badd +0 output.txt
argglobal
%argdel
$argadd project.py
set stal=2
tabnew +setlocal\ bufhidden=wipe
tabrewind
edit project.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 37 + 24) / 49)
exe 'vert 1resize ' . ((&columns * 146 + 95) / 190)
exe '2resize ' . ((&lines * 8 + 24) / 49)
exe 'vert 2resize ' . ((&columns * 146 + 95) / 190)
exe '3resize ' . ((&lines * 23 + 24) / 49)
exe 'vert 3resize ' . ((&columns * 43 + 95) / 190)
exe '4resize ' . ((&lines * 22 + 24) / 49)
exe 'vert 4resize ' . ((&columns * 43 + 95) / 190)
argglobal
balt HORMONE.csv
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 8 - ((7 * winheight(0) + 18) / 37)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("pandas_df_operations.md", ":p")) | buffer pandas_df_operations.md | else | edit pandas_df_operations.md | endif
if &buftype ==# 'terminal'
  silent file pandas_df_operations.md
endif
balt project.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 25 - ((5 * winheight(0) + 4) / 8)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 25
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("HORMONE.csv", ":p")) | buffer HORMONE.csv | else | edit HORMONE.csv | endif
if &buftype ==# 'terminal'
  silent file HORMONE.csv
endif
balt project.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 397 - ((9 * winheight(0) + 11) / 23)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 397
normal! 08|
wincmd w
argglobal
if bufexists(fnamemodify("hormone.txt", ":p")) | buffer hormone.txt | else | edit hormone.txt | endif
if &buftype ==# 'terminal'
  silent file hormone.txt
endif
balt HORMONE.csv
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 7 - ((3 * winheight(0) + 11) / 22)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 7
normal! 019|
wincmd w
exe '1resize ' . ((&lines * 37 + 24) / 49)
exe 'vert 1resize ' . ((&columns * 146 + 95) / 190)
exe '2resize ' . ((&lines * 8 + 24) / 49)
exe 'vert 2resize ' . ((&columns * 146 + 95) / 190)
exe '3resize ' . ((&lines * 23 + 24) / 49)
exe 'vert 3resize ' . ((&columns * 43 + 95) / 190)
exe '4resize ' . ((&lines * 22 + 24) / 49)
exe 'vert 4resize ' . ((&columns * 43 + 95) / 190)
tabnext
edit output.txt
argglobal
balt term://~/school/Math-2050/project_2//121004:/bin/bash
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 39 - ((29 * winheight(0) + 23) / 46)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 39
normal! 019|
tabnext 2
set stal=1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
