Title: tikz cookbook
Author: SergeM
Date: 2014-07-16 23:44:00
Slug: tikz-cookbook
Tags: useful,latex,tikz


[Drawing on an image with TikZ](http://tex.stackexchange.com/questions/9559/drawing-on-an-image-with-tikz)
http://tex.stackexchange.com/questions/9559/drawing-on-an-image-with-tikz

Drawing label on figure (using tikz)
\begin{tikzpicture}
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; \node[anchor=south west,inner sep=0] at (0,0) {\includegraphics[trim={600px 200px 50px 200px},clip, width=1\linewidth]{images/DP_10150_simpleCombinedBasedOnDPlen.exe_scale1_blank/frm00001}};
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; %\draw[white,fill=white] (0.0,0.0) rectangle (0.5,0.5);
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; \node[minimum size=.6cm, fill=white,anchor=south west] at (0.0,0.0){а};&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; \end{tikzpicture} 

</div>