# Real Analysis Qualifying Examination

Fall, 2020

Name ID number

<table><tr><td rowspan=1 colspan=1>Problem</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>Total</td></tr><tr><td rowspan=1 colspan=1>Score</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

## Instructions

• This is a three-hour Zoom exam without recording.

o Please keep your video on during the entire exam but do not expose your exam to the Zoom camera.

o Please submit your questions through the Zoom chat.

o Please submit your exam to the google drive folder:

RealAnal_QualExam_YourInitial.

Your submission of the exam is final: once your submit it, you cannot make any changes to the exam and you cannot re-submit a new exam.

o In case any technical problems occur, please email the instructor (bli@ucsd.edu).

o Follow-up oral exams are reserved to check the academic integrity.

• There are 3 pages of this set of exam instructions and problems (including this coversheet).
The exam has 7 problems of total 200 points.
To get credit, you must show your work.
Partial credit will be given to partial answers.

• This is an open-book and open-note but no-calculator exam.
You can look at the textbook (Folland’s Real Analysis) and your own notes on this textbook.
You cannot look at any other material (including your own homework solutions, the instructor’s notes, the instructor’s homework solutions, and other online material).
No internet search for other material is allowed.
No discussions are allowed.

• Please note:

o You may use, without proof, any results proved in the textbook (Folland’s Real Analysis).
If you use such a result, please cite it by its name (if it has one) or explain what it is concisely.
Please also verify explicitly all the hypotheses in the statement.

o You need to re-prove any result given as a homework problem, unless it is a statement proved in the text.

o If the statement you are asked to prove is exactly a result in the text, you still need to provide a proof instead of just citing the result.

• Unless otherwise stated, standard notations as in the textbook (Folland’s Real Analysis) will be used.
In particular, we denote by m the Lebesgue measure.

Problem 1 (60 points).
Determine if each of the following statements is true or false.
If your answer is true, then please give a brief proof.
If your answer is false, then please give a counterexample or prove your assertion.
For your proof, you may cite a proved result from the text with a brief explanation how the conclusion follows.

(1) Let X be a Banach space and A a closed subset of X. Then A is sequentially weakly closed, i.e., if $u _ { n } \in A ( n = 1 , 2 , . . . )$ and $u _ { n } \to u$ weakly for some $u \in X$ , then $u \in A$

(2) Let X be a compact Hausdorff topological space.
Let $K _ { j } \ ( j = 1 , 2 , \ldots )$ be a sequence of decreasing, nonempty compact subsets of X. Then $\cap _ { j = 1 } ^ { \infty } K _ { j } \neq \emptyset$

(3) Let X be a locally compact Hausdorff space and $M ( X )$ the Banach space of all complex Radon measures on X. Let $\mu \in M ( X )$ and $\mu _ { n } \in M ( X ) \ ( n = 1 , 2 , . . . )$ and assume that $\mu _ { n } \to \mu$ vaguely in $M ( X )$ . Then $\mu _ { n } ( E ) \to \mu ( E )$ for any Borel set $E \subseteq X$

(4) Let S denote the Schwartz space on $\mathbb { R } ^ { n }$ . Let $f , g \in S$ . If $f * g = 0$ in $\mathbb { R } ^ { n }$ then either $f = 0$ identically in $\mathbb { R } ^ { n }$ or $g = 0$ identically in $\mathbb { R } ^ { n }$

Problem 2 (20 points).
Let X denote the set of all sequences $a = ( a _ { 1 } , a _ { 2 } , \dots )$ with all $a _ { k }$ $( k \geq 1 )$ real numbers but only finitely many of them nonzero.
X is a real vector space with the usual component-wise addition and scalar multiplication.
It is a normed vector space with the norm $\left\| a \right\| = \operatorname* { s u p } _ { k \geq 1 } \left| a _ { k } \right|$ . Define $T : X  X$ by

$$
T a = \left( a _ { 1 } , { \frac { 1 } { 2 } } a _ { 2 } , \ldots , { \frac { 1 } { k } } a _ { k } , \ldots \right) \quad { \mathrm { i f ~ } } a = ( a _ { 1 } , a _ { 2 } , \ldots , a _ { k } , \ldots ) \in X .
$$

Prove that $T : X  X$ is a bijective, linear, and bounded operator, but its inverse $T ^ { - 1 } : X \to X$ is unbounded.

Problem 3 (20 points) Let $f \in L ^ { 1 } ( \mathbb { R } ^ { n } )$ and $f > 0$ in $\mathbb { R } ^ { n }$ . Prove that the strict inequality $| { \hat { f } } ( \xi ) | < { \hat { f } } ( 0 )$ holds for any $\xi \in \mathbb { R } ^ { n }$ with $\xi \neq 0$ •

Problem 4 (25 points).
Let $( X , { \mathcal { M } } , \mu )$ be a finite measure space.
Prove the following:

(1) If $f \in L ^ { 1 } ( \mu )$ and $f \geq 0$ on X, then $f ^ { \alpha } \in L ^ { 1 } ( \mu )$ for any $\alpha \in ( 0 , 1 )$ and

$$
\operatorname* { l i m } _ { \alpha \to 0 + } \int _ { X } f ^ { \alpha } d \mu = \mu ( \{ x \in X : f ( x ) > 0 \} ) .
$$

(2) If $g \in L ^ { \infty } ( \mu )$ with $\| g \| _ { \infty } > 0$ , then $g \in L ^ { p } ( \mu )$ for any $p \in [ 1 , \infty )$ and

$$
\operatorname* { l i m } _ { p \to + \infty } { \frac { \displaystyle \int _ { X } | g | ^ { p + 1 } d \mu } { \displaystyle \int _ { X } | g | ^ { p } d \mu } } = \| g \| _ { \infty } .
$$

Problem 5 (25 points) Let $\mu$ be a (positive) Borel measure on [0, 1] and denote by m the Lebesgue measure.
Assume

$$
\left| \int _ { [ 0 , 1 ] } f ^ { \prime } d \mu \right| \leq \left( \int _ { [ 0 , 1 ] } f ^ { 2 } d m \right) ^ { 1 / 2 } \qquad \forall f \in C ^ { 1 } ( [ 0 , 1 ] ) .
$$

Prove the following:

(1) $\mu \ll m ;$

(2) If $u = d \mu / d m \in L ^ { 1 } ( m )$ is the Radon–Nikodym derivative of $\mu$ with respect to $m _ { : }$ , then

$$
| u ( x ) - u ( y ) | \leq | x - y | ^ { 1 / 2 } \qquad { \mathrm { f o r ~ a . e . ~ } } x , y \in [ 0 , 1 ] .
$$

Problem 6 (25 points).
Let X be a real Banach space and $x _ { k } \in X \ ( k = 1 , 2 , . . . )$ . Assume that $\textstyle \sum _ { k = 1 } ^ { \infty } | f ( x _ { k } ) | < \infty$ for any $f \in X ^ { * }$ . Prove that there exists a constant $\gamma \geq 0$ such that $\textstyle \sum _ { k = 1 } ^ { \infty } | { \dot { f } } ( { \bar { x _ { k } } } ) | \leq \gamma \| f \|$ for any $f \in X ^ { * }$

Problem 7 (25 points).
Let X be a locally compact Hausdorff topological vector space.
Let $f \in C _ { 0 } ( X )$ and $f _ { k } \in C _ { 0 } ( X ) \ ( k = 1 , 2 , \dots )$ . Prove that $f _ { k }  f$ weakly in $C _ { 0 } ( X )$ if and only if $\mathrm { s u p } _ { k \geq 1 } \| f _ { k } \| _ { u } < \infty$ and $f _ { k }  f$ pointwise on $X$
