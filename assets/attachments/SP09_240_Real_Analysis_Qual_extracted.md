C
<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>Points</td></tr><tr><td rowspan=1 colspan=1>Page 2(14 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 3(14 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 4(7 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 5(15 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 6(10 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 7(15 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 8(15 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Page 9(10 points)</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>Total(100 points)</td><td rowspan=1 colspan=1></td></tr></table>

General instructions: 3 hours. Be sure to carefully motivate all (nontrivial) claims and statements. You may use without proof any result proved in the text (as well as ones covered in the lecture). If you use a theorem from the text (or lecture), refer to it either by name (if it has one) or explain what it says. Also verify explicitly all hypotheses in the theorem. You need to reprove any result given as an exercise (unless it has been singled out and lectured upon). If the statement you are asked to prove is exactly a result covered in the class you are asked to re-construct the proof instead of citing the result. m (or dm) denotes the Lebesgue measure.

(1) Determine if the statements below are True or False. If True, give a brief proof. If False, give a counterexample (or prove your assertion in another way, if you prefer). If your claim follows from a theorem in the text, name the theorem (or describe it otherwise) and explain carefully how the conclusion follows.

a) (7 pts) There does not exist a Lebesgue integrable function $f \in L ^ { 1 } ( \mathbb { R } )$ such that for any $A > 0$ and any interval (a, b), $m ( \left\{ x \in ( a , b ) \mid f ( x ) > A \right\} ) > 0$

b) (7 pts) Let $\mu ( A ) \doteq \# A$ be the counting measure and $\Delta = \{ ( x , y ) \in [ 0 , 1 ] ^ { 2 } | x =$ $y \}$ the diagonal in $\{ 0 , 1 \} ^ { 2 }$ . Then by Tonelli-Fubini theorem, the iterated integrals

$$
\int _ { 0 } ^ { 1 } \left[ \int _ { 0 } ^ { 1 } \chi _ { \Delta } ( x , y ) d m ( x ) \right] d \mu ( y ) = \int _ { 0 } ^ { 1 } \left[ \int _ { 0 } ^ { 1 } \chi _ { \Delta } ( x , y ) d \mu ( y ) \right] d m ( x ) .
$$

Here m is the Lebesgue measure, $\chi _ { \Delta }$ is the characteristic function of $\Delta$

c) (7 pts) Let v be a signed measure and $\mu$ be a positive measure. Then $\nu < < \mu$ if any only if $\nu ^ { + } < < \mu$ and $\nu ^ { - } < < \mu$

(7 pts) Let $f _ { n }$ and $g _ { n }$ are real-valued Lebesgue measurable functions on $\mathbb { R } ^ { 1 }$ Assume that $f _ { n } \to f$ and $g _ { n }  g$ in measure, then $f _ { n } g _ { n } \to f g$ in measure.

e) (7 pts) Let Ω be a bounded domain in Rn. If $f _ { n } \in L ^ { p } ( \Omega )$ for $1 < p < \infty$ and converges weakly to $f \in L ^ { p } ( \Omega )$ , then $\| f \| _ { p } \leq$ lim inf $\gamma _ { l \longrightarrow \infty } \Vert f _ { n _ { 1 } ; p } .$

(2Assume that $X , Y , Z$ are Banach spaces. Assume $\Phi : X \times Y ^ { \prime }  Z$ is bilinear, namely for every $x \in { \mathrm { . Y } } , \Phi ( x , \cdot ) : Y \to Z$ is linear and for every $y \in \Sigma ^ { \cdot } , \Phi ( \cdot , y ) : . \mathrm { { X }  { Z } }$ is linear. Show that if for every $z ^ { * } \in Z ^ { * } , z ^ { * } ( \Phi ( x , \cdot ) ) \in Y ^ { * } \ \mathrm { a n d } \ z ^ { * } ( \Phi ( \cdot , y ) ) \in X ^ { * }$ , then 1) (7 pts) $\psi _ { x } ( \cdot ) \div \Phi ( x , \cdot ) : Y  Z$ and $\psi _ { y } ( \cdot ) \doteq \Phi ( \cdot , y ) : X \to Z$ are bounded linear maps;

2) (8 pts) there exists M such that

$$
\| \Phi ( x , y ) \| \leq M \| x \| \| y \| .
$$

(3 (10 pts) Assume that $1 \leq p < \infty$ and $( X , { \mathcal { M } } , \mu )$ is a measure space. If $f _ { n } \to f$ in measure and $\vert f _ { n } \vert \leq g \in L ^ { p } ( . \mathrm { Y } , d \mu )$ for all n. Then $f _ { n } \to f$ in $L ^ { p } { \mathrm { - n o r m } }$

(4) (15 pts) Show that on $\Re ^ { 2 }$ (with coordinates $\left( x _ { 1 } , x _ { 2 } \right) ,$ ,

$$
\langle \mathrm { P V } \left( { \frac { x _ { 1 } + x _ { 2 } } { | x | ^ { 3 } } } \right) , \phi \rangle \doteq \operatorname* { l i m } _ { \epsilon \to 0 } \int _ { | x | > \epsilon } \phi ( x ) { \frac { x _ { 1 } + x _ { 2 } } { | x | ^ { 3 } } } d m , \quad \phi \in C _ { c } ^ { \infty } ( \mathbb { R } ^ { 2 } ) ,
$$

exists and defines a distribution on $\mathbb { R } ^ { 2 }$