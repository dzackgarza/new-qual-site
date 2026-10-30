# Math 202 Qualifying Exam, Spring 2020

June 3 2020, 09:00 AM – 12:00 noon.

• Complete the following problems, or as much of them as you can. There are eight problems carrying 25 points each. In order to receive full credit, please show all of your work and justify your answers. Partial answers may receive partial credit.

• You may use any result proved in lectures, a textbook, problem sets, or any other clearly referenced source; provided it is true, and unless (i) you are specifically instructed not to, or (ii) the result renders the question entirely trivial, e.g. because the question asks you to prove that result. You should state results clearly before using them.

• Insofar as it makes sense in context, you may answer later parts of a question (for full credit) without having correctly answered previous parts, and in your answer you may assume the conclusions of previous parts.

• You may consult textbooks or your own notes. You must indicate clearly when outside references are used in your answers.

• You may not consult the internet—e.g., to search for or access online resources—during the exam.

• You may not seek assistance from other people during the exam (including electronically).

• You have 3 hours. When you are finished, please upload your solutions to Gradescope.

• You should record your answers on your own paper, or digital paper equivalent. Please indicate clearly (on your script as well as on Gradescope) which pages correspond to which questions.

• Under all circumstances, remain calm.

1. (25 points) Let $\phi \colon \mathbb { C } ^ { 8 } \to \mathbb { C } ^ { 8 }$ be a linear map whose matrix with respect to the standard basis is of the form

$$
\left( { \begin{array} { l l l l l l l l } { 1 } & { * } & { * } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 1 } & { * } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 1 } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 1 } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} } \right)
$$

where $^ { 6 6 } \ast ^ { 5 9 }$ represents an unknown value. Suppose moreover that we are told

$$
\begin{array} { r } { \mathrm { d i m } \mathrm { k e r } \phi = 2 } \\ { \mathrm { d i m } \mathrm { k e r } ( \phi - \mathrm { i d } ) = 2 } \\ { \phi ^ { 5 } - 2 \phi ^ { 4 } + \phi ^ { 3 } = 0 . } \end{array}
$$

Determine, with proof, the maximum and minumum possible values of

$$
\dim \ker ( \phi ^ { 2 } ) { \mathrm { ~ a n d ~ } } \dim \ker \big ( ( \phi - \operatorname { i d } ) ^ { 2 } \big ) .
$$

2. Suppose $\mathbb { C } ^ { 1 0 }$ has its usual inner product and $\phi , \psi \colon \mathbb { C } ^ { 1 0 } \to \mathbb { C } ^ { 1 0 }$ are two linear maps. Suppose that the singular values of $\phi$ are given by $\sigma _ { i } ( \phi ) = 1 1 - i$ for $1 \leq i \leq 1 0 ;$ i.e.,

$$
\sigma _ { 1 } ( \phi ) = 1 0 , \sigma _ { 2 } ( \phi ) = 9 , \sigma _ { 3 } ( \phi ) = 8 , . . . , \sigma _ { 1 0 } ( \phi ) = 1 ;
$$

and that the Frobenius norm $\lVert \psi \rVert _ { \mathrm { F r o b } }$ is exactly 1.

(a) (12 points) Show that dim ker $( \phi + \psi ) \leq 1$

(b) (13 points) Show that if dim ker $\textstyle ( \phi + \psi ) = 1$ then $\psi$ has rank 1.

Total for Question 2: (25 points)

3. (25 points) Let V be an inner product space of dimension $n ,$ and $\phi , \psi \colon V \to V$ two positive definite Hermition maps. You may use without proof that ψ has a unique positive definite square root $\psi ^ { 1 / 2 }$ , and that $\psi$ and $\psi ^ { 1 / 2 }$ are non-singular.

Let $t \in \mathbb { R }$ be a real number. Prove that $\phi - t \psi$ is positive definite if and only if $t < \lambda _ { n } ( \theta )$ (i.e., the smallest eigenvalue of θ) where $\theta = \psi ^ { - 1 / 2 } \phi \psi ^ { - \bar { 1 / 2 } }$

4. (25 points) Here is the character table for some group of size 360 (rows are characters, the columns are conjugacy classes):

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>γ1</td><td rowspan=1 colspan=1>γ2</td><td rowspan=1 colspan=1>γ3</td><td rowspan=1 colspan=1>γ4</td><td rowspan=1 colspan=1>γ5</td><td rowspan=1 colspan=1> $\gamma _ { 6 }$ </td><td rowspan=1 colspan=1>γ7</td></tr><tr><td rowspan=3 colspan=1>χ1χ2χ3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>1</td><td rowspan=3 colspan=1>01+√srt5 }$21-√\sqrt{5 }$2</td><td rowspan=5 colspan=1>01-√srt5 }$21+√sqrt{5 }$2−10</td></tr><tr><td rowspan=1 colspan=1>χ4</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>X5</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>X6</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>−1</td></tr><tr><td rowspan=1 colspan=1>X7</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>−2</td><td rowspan=1 colspan=1>0</td></tr></table>

Determine the sizes of its conjugacy classes. For your convenience, the divisors of 360 are: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360.

5. (a) (10 points) Let X be the set of 4-element subsets of $\{ 1 , \ldots , 7 \}$ with the action of the symmetric group ${ \mathfrak { S } } _ { 7 }$ via permuting values. What is the decomposition of the permutation representation $\mathbb { C } [ X ]$ into irreducible representations?

(b) (10 points) Let Y be the set of pairs $( S , \sigma )$ where S is a 4-element subset of $\{ 1 , \ldots , 7 \}$ and σ is an ordering of $\{ 1 , \ldots , 7 \} \setminus S$ , again with the action of the symmetric group ${ \mathfrak { S } } _ { 7 }$ via permuting values. What is the decomposition of the permutation representation $\mathbb { C } [ Y ]$ into irreducible representations?

(c) (5 points) Explain what computation regarding polynomial functors the above two problems can be used to solve.

Total for Question 5: (25 points)

6. Let h, i be the scalar product on the ring of symmetric functions.

(a) (10 points) Evaluate $\langle e _ { 1 } ^ { n } , e _ { 1 } ^ { n } \rangle$

(b) (15 points) Evaluate $\langle h _ { 3 } p _ { 6 } , s _ { 5 , 4 } \rangle$

Total for Question 6: (25 points)

7. (25 points) Let (H, U) be a unitary representation of a compact group G. Show that the operator $\textstyle P = \int _ { \mathrm { G } } U ( g ) \mathrm { d } g$ is the orthogonal projection of H onto the space of G-invariants in H.

8. (25 points) Compute the integrals

$$
\int _ { \mathrm { U ( 2 ) } } \mathrm { T r } U \mathrm { d } U \quad \mathrm { a n d } \quad \int _ { \mathrm { U ( 2 ) } } | u _ { 1 1 } | ^ { 2 } \mathrm { d } U ,
$$

where the integration is over the group of $2 \times 2$ unitary matrices $U = \left[ \begin{array} { l l } { u _ { 1 1 } } & { u _ { 1 2 } } \\ { u _ { 2 1 } } & { u _ { 2 2 } } \end{array} \right]$ against Haar measure.

## End of Examination