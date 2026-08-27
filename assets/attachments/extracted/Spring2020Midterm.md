# MATH 8150 Midterm Exam — Spring 2020 Instructor: Prof. Jingzhi Tie

Please read the UGA Student Honor Code: “I will be academically honest in all of my academic work and will not tolerate academic dishonesty of others.”

SIGNATURE:

Print Your Name:

Due date: April 20, 2020

You can freely use the theorems we have covered in the semester (either proved in the text or in class). Clearly label each problem in your paper. Cross out the parts you do not want to be graded.

<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>Points</td><td rowspan=1 colspan=1>Score</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Total</td><td rowspan=1 colspan=1>120</td><td rowspan=1 colspan=1></td></tr></table>

1. Prove that the distinct complex numbers $z _ { 1 } , z _ { 2 }$ and $z _ { 3 }$ are the vertices of an equilateral triangel if and only if

$$
z _ { 1 } ^ { 2 } + z _ { 2 } ^ { 2 } + z _ { 3 } ^ { 2 } = z _ { 1 } z _ { 2 } + z _ { 2 } z _ { 3 } + z _ { 3 } z _ { 1 } .
$$

2. Let $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ be analytic and one-to-one in $| z | < 1$ . For $0 < r _ { 0 } < 1$ , let $\overline { { D } } _ { r _ { 0 } }$ be the closed disk $| z | \leq r _ { 0 }$ . Show that the area A of $f ( \overline { { D } } _ { r _ { 0 } } )$ is finite and is given by

$$
A = \pi \sum _ { n = 1 } ^ { \infty } n | c _ { n } | ^ { 2 } r _ { 0 } ^ { 2 n } .
$$

[Hint: First find a formula in terms of polar coordinates in xy-plane for the area element dudv using complex analysis, where $f = u + i v$ . Note that $d x d y = r d r d \theta . ]$

3. Assume f is continuous in the region: $R _ { 0 } \leq | z - a | < \infty , \ 0 \leq \arg ( z - a ) \leq \beta _ { 0 }$ $( 0 < \beta _ { 0 } \le 2 \pi )$ and the limit $\operatorname* { l i m } _ { z \to \infty } ( z - a ) f ( z ) = A$ exists. Show that

$$
\operatorname* { l i m } _ { r  + \infty } \int _ { \gamma { r } } f ( z ) d z = i A \beta _ { 0 } ,
$$

where $\gamma _ { r } : = \lbrace z \mid z = a + r e ^ { i t } , 0 \leq t \leq \beta _ { 0 } \rbrace$

4. Computer the integral $I ( b ) = \int _ { 0 } ^ { \frac { \pi } { 2 } } ( \tan t ) ^ { i b } d t$ for $b \in \mathbb { R }$ . Hint: Some simple substitution will reduce the integral to what we have done in homework and lectures.

5. Let $f ( z ) = 2 z ^ { 5 } + 8 z - 1$ . Show that all five zeros of $f ( z )$ are inside the disk $D ( 0 , 2 )$ and only one zero is inside the disk $D ( 0 , 1 )$ •

6. (Cauchy’s formula for “exterior” region) Let γ be piecewise smooth simple closed curve with interior $\Omega _ { 1 }$ and exterior $\Omega _ { 2 }$ . Assume $f ^ { \prime } ( z )$ exists in an open set containing $\gamma$ and $\Omega _ { 2 }$ and $\begin{array} { r } { \operatorname* { l i m } _ { z \to \infty } f ( z ) = A } \end{array}$ . Show that

$$
{ \frac { 1 } { 2 \pi i } } \int _ { \gamma } { \frac { f ( \xi ) } { \xi - z } } d \xi = { \left\{ \begin{array} { l l } { A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 1 } , } \\ { - f ( z ) + A , } & { { \mathrm { i f ~ } } z \in \Omega _ { 2 } } \end{array} \right. }
$$