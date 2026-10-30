# Real Analysis Qualifying Examination Spring, 2020

Name ID number

<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Total</td></tr><tr><td rowspan=1 colspan=1>Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

## Instructions

• This is a three-hour Zoom exam without recording.

o Please keep your video on during the entire exam but do not expose your exam to the Zoom camera.

o Please submit your questions through the Zoom chat.

o Please submit your exam to the google drive folder:

RealAnal_QualExam_YourFirstName_YourLastName.

Your submission of the exam is final: once your submit it, you cannot make any changes to the exam and you cannot re-submit a new exam.

o In case any technical problems occur, please email the instructor (bli@ucsd.edu).

o Follow-up oral exams are reserved to check the academic integrity.

• There are 3 pages of this set of exam instructions and problems (including this coversheet). The exam has 7 problems of total 200 points. To get credit, you must show your work. Partial credit will be given to partial answers.

• This is an open-book and open-note but no-calculator exam. You can look at the textbook (Folland’s Real Analysis) and your own notes. You cannot look at any other material (including your own homework solutions, the instructor’s notes, the instructor’s homework solutions, and other online material). No internet search for other material is allowed. No discussions are allowed.

• Please note:

o You may use, without proof, any results proved in the textbook or covered in the lecture. If you use such a result, please cite it by its name (if it has one) or explain what it is concisely. Please also verify explicitly all the hypotheses in the statement.

o You need to re-prove any result given as a homework problem, unless it is a statement proved in the text or in the lecture.

o If the statement you are asked to prove is exactly a result in the text or covered in the class, you still need to provide a proof instead of just citing the result.

• Unless otherwise stated, standard notations as in the textbook (Folland’s Real Analysis) will be used. In particular, we denote by m the Lebesgue measure.

Problem 1 (50 points). Determine if each of the following statements is true or false. If your answer is true, then please give a brief proof. If your answer is false, then please give a counterexample or prove your assertion. For your proof, you may cite a proved result from the text, with a brief explanation how the conclusion follows.

(1) Let E be a Lebesgue-measurable subset of R. For each $k \in \mathbb N$ , let $E _ { k } \ = \ \{ x \in \mathbb { R }$ dist $( x , E ) < 1 / k \}$ , where dist $( x , E ) = \operatorname* { i n f } \{ | y - x | : y \in E \}$ . Then $\begin{array} { r } { \operatorname* { l i m } _ { k  \infty } m ( E _ { k } ) = m ( E ) } \end{array}$

(2) If $f : ( 0 , 1 ) $ R is differentiable at each point $x \in ( 0 , 1 )$ , then the derivative $f ^ { \prime } : ( 0 , 1 ) \to \mathbb { R }$ is Borel-measurable on (0, 1).

(3) Let $( X , { \mathcal { M } } , \mu )$ be a measure space with $\mu ( X ) = 1$ . Let $E _ { j } \in \mathcal { M } \ ( j = 1 , \ldots , n )$ . Let $q$ be an integer such that $1 \leq q \leq n$ . Assume that any $x \in X$ belongs to at least $q$ of these subsets $\begin{array} { r } { E _ { 1 } , \ldots , E _ { n } , \mathrm { { i . e . , } } x \in \bigcap _ { i = 1 } ^ { q } E _ { j _ { i } } } \end{array}$ with $j _ { 1 } , \dots , j _ { q }$ distinct indices (that may depend on x). Then there exists $j _ { 0 }$ such that $\mu ( E _ { j _ { 0 } } ) \geq q / n$

(4) The space $C ( [ 0 , 1 ] )$ is a closed subspace of $L ^ { 1 } ( [ 0 , 1 ] , m )$ (m is the Lebesgue measure) with respect to the $L ^ { 1 } ( [ 0 , 1 ] , m )  – \mathrm { n o r m }$

Problem 2 (30 points). There are three sub-problems here; and all of them are of calculation type. Please justify your calculations.

(1) Let $f \in L ^ { \infty } ( \mathbb { R } )$ and $g \in L ^ { 1 } ( \mathbb { R } )$ with respect to the Lebesgue measure m. Assume that f is continuous at $x = 1$ with $f ( 1 ) = \pi$ and that $g \geq 0$ on R and $\| g \| _ { L ^ { 1 } ( \mathbb { R } ) } = 2$ . Calculate

$$
\operatorname* { l i m } _ { k \to + \infty } \int _ { [ - k , k ] } f \left( 1 + { \frac { x ^ { 2 } } { k } } \right) g ( x ) d m ( x ) .
$$

(2) Let $\mu$ be the Lebesgue–Stieltjes measure associated to the following increasing and rightcontinuous function $F : \mathbb { R }  \mathbb { R }$ :

$$
F ( x ) = { \left\{ \begin{array} { l l } { 0 } & { { \mathrm { ~ i f ~ } } x < 0 , } \\ { x + 2 } & { { \mathrm { ~ i f ~ } } 0 \leq x < 1 , } \\ { 4 x ^ { 2 } } & { { \mathrm { ~ i f ~ } } 1 \leq x < \infty . } \end{array} \right. }
$$

Calculate $\mu ( ( - \infty , 0 ] ) , \mu ( \{ 1 \} )$ , and $\mu ( [ 1 , 2 ] )$ .

(3) Let E be a Lebesgue-measurable subset of $[ 0 , 1 ]$ with the Lebesgue measure $m ( E ) = 1 / 2$ Let $u _ { k } \in \mathbb { R } \ ( k = 1 , 2 , . . . )$ . Calculate

$$
\operatorname* { l i m } _ { k \to \infty } \int _ { E } \cos ^ { 2 } ( k \pi x + u _ { k } ) d m ( x ) .
$$

Problem 3 (20 points). Consider the Lebesgue measure m on $[ 0 , 1 ]$ and denote by $\| \cdot \| _ { p }$ the $L ^ { p } ( [ 0 , 1 ] )$ -norm for any $p \in [ 1 , \infty ]$ Define $B = \{ f \in L ^ { 2 } ( [ 0 , 1 ] ) : \bar { \| } f \| _ { 2 } ^ { \cdot } \leq 1 \}$ . It is clear that B is a subset of $L ^ { 1 } ( [ 0 , 1 ] )$ . Prove that, with respect to the $L ^ { 1 } ( [ 0 , 1 ] )$ )-norm, B is closed and has an empty interior.

Problem 4 (25 points). Let X be a locally compact Hausdorff space and µ a Radon measure on X. Assume that $\mu ( X ) = \infty$ . Let $A _ { n } > 0 ( n = 1 , 2 , . . . )$ . Prove that for each $n \in \mathbb N$ there exist a compact subset $K _ { n }$ of X, a precompact open subset $U _ { n }$ of X, and a function $f _ { n } \in C _ { \mathrm { c } } ( X , [ 0 , 1 ] )$ such that $\mu ( K _ { n } ) > A _ { n }$ and $K _ { n } \prec f _ { n } \prec U _ { n } { \mathrm { ~ ( i . e . , ~ } } f _ { n } = 1$ on $K _ { n }$ and supp $( f _ { n } ) \subseteq U _ { n } )$ , and that all the open subsets $U _ { n } \ ( n = 1 , 2 , \ldots )$ are pairwise disjoint.

Problem 5 (25 points). Let $f \in C ^ { 1 } ( \mathbb { T } )$ . Let ${ \widehat { f } } ( k ) \ ( k \in \mathbb { Z } )$ be the Fourier coefficients of $f .$ Prove that

$$
\sum _ { k = - \infty } ^ { \infty } \Big | \widehat { f } ( k ) \Big | \leq \| f \| _ { L ^ { 1 } ( \mathbb { T } ) } + \frac { 1 } { \sqrt { 2 } \pi } \| f ^ { \prime } \| _ { L ^ { 2 } ( \mathbb { T } ) } \sqrt { \sum _ { k = 1 } ^ { \infty } \frac { 1 } { k ^ { 2 } } } .
$$

Problem 6 (25 points). Let ${ { c } _ { n } } \in \mathbb { R } \ ( n = 0 , 1 , 2 , . . . )$ . Prove that the following two conditions (1) and (2) are equivalent:

(1) There exists a signed Radon measure µ on $[ 0 , 1 ]$ such that

$$
\int _ { [ 0 , 1 ] } t ^ { n } d \mu ( t ) = c _ { n } \qquad ( n = 0 , 1 , \ldots ) ;
$$

(2) There exists $M \geq 0$ such that for any $N \in  { \mathbb { N } }$ and any $a _ { n } \in \mathbb { R } \ ( n = 0 , \dots , N )$

$$
\left| \sum _ { n = 0 } ^ { N } a _ { n } c _ { n } \right| \leq M \operatorname* { m a x } _ { 0 \leq t \leq 1 } \left| \sum _ { n = 0 } ^ { N } a _ { n } t ^ { n } \right| .
$$

Problem 7 (25 points). Let H be a real Hilbert space. Recall the following result (you can cite it, if needed, without proof): If K is a nonempty, closed, and convex subset of H, and $x \in H \backslash K$ , then there exists a unique $y \in K$ such that $\begin{array} { r } { \| x - y \| = \operatorname* { m i n } _ { z \in K } \| x - z \| } \end{array}$ . Moreover,

$$
\langle x - y , z - y \rangle \leq 0 \qquad \forall z \in K .
$$

(1) Let K be a nonempty, closed, and convex subset of H. Prove that K is weakly sequentially closed, ${ \mathrm { i . e . , i f ~ } } u _ { n } \in K { \mathrm { ~ } } ( n = 1 , 2 , . . . )$ and $u \in H$ satisfy that $u _ { n } \to u$ weakly, then $u \in K$

$$
K _ { n } \ ( n = 1 , 2 , \ldots )
$$

$$
K _ { n + 1 } \subseteq K _ { n } \ ( n = 1 , 2 , . . . )
$$

$$
\cap _ { k = n } ^ { \infty } K _ { n } \neq \emptyset
$$