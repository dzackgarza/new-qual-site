# Math 202 Qualifying Exam, Fall 2020

## Friday September 4 2020, 5:00 PM – 8:00 PM PDT.

• Complete the following problems, or as much of them as you can. There are eight problems carrying 25 points each. In order to receive full credit, please show all of your work and justify your answers. Partial answers may receive partial credit.

• You may use any result proved in lectures, a textbook, problem sets, or any other clearly referenced source; provided it is true, and unless (i) you are specifically instructed not to, or (ii) the result renders the question entirely trivial, e.g. because the question asks you to prove that result. You should state results clearly before using them.

• Insofar as it makes sense in context, you may answer later parts of a question (for full credit) without having correctly answered previous parts, and in your answer you may assume the conclusions of previous parts.

• You may consult textbooks or your own notes. You must indicate clearly when outside references are used in your answers.

• You may not consult the internet—e.g., to search for or access online resources—during the exam.

• You may not seek assistance from other people during the exam (including electronically).

• You have 3 hours. When you are finished, please upload your solutions to Gradescope.

• You should record your answers on your own paper, or digital paper equivalent. Please indicate clearly (on your script as well as on Gradescope) which pages correspond to which questions.

• Under all circumstances, remain calm.

1. A linear map $\phi \colon \mathbb { C } ^ { 2 0 } \to \mathbb { C } ^ { 2 0 }$ has the property that $\phi ^ { 3 } = \phi ^ { 2 }$

(a) (8 points) Show that if λ is an eigenvalue of $\phi$ then $\lambda = 0$ or $\lambda = 1$

Now suppose furthermore that dim $E ( 0 , \phi )$ = dim $E ( 1 , \phi ) = 8$

[Here $E ( \lambda , \phi ) \subseteq \mathbb { C } ^ { 2 0 }$ denotes the eigenspace of $\phi$ with eigenvalue $\lambda . ]$

(b) (17 points) Find, with justification, the Jordan Normal Form of $\phi$

[For this question, “find the Jordan Normal form” means you should determine the sizes and multiplicities of the Jordan blocks. You should not attempt to describe a basis that puts $\phi$ in Jordan Normal Form.]

Total for Question 1: (25 points)

2. Suppose $\mathbb { C } ^ { 3 }$ is given its usual inner product, and $\psi \colon \mathbb { C } ^ { 3 } \to \mathbb { C } ^ { 3 }$ is a linear map. Further suppose that the singular values of $\psi$ are $\sigma _ { 1 } = 3 , \sigma _ { 2 } = 2$ and $\sigma _ { 3 } = 1$

(a) (5 points) Determine, with justification, the norms $\| \psi \| _ { \mathrm { o p } }$ and $\| \psi \| _ { \mathrm { F r o b } }$

(b) (10 points) Let $\lambda \in \mathbb { C }$ be an eigenvalue of $\psi .$ . Prove that $| \lambda | \in [ 1 , 3 ]$

(c) (10 points) Suppose now that $\psi$ is self-adjoint. Prove that $\lambda \in \{ - 3 , - 2 , - 1 , 1 , 2 , 3 \}$

Total for Question 2: (25 points)

3. Let V be a finite-dimensional inner product space and $\alpha , \beta \colon V \to V$ two positive definite selfadjoint linear maps. We write $\alpha ^ { 1 / 2 }$ to denote the unique positive definite square-root of $\alpha ;$ you may assume without proof that this exists.

(a) (5 points) Give an example to show that $\alpha \circ \beta \colon V  V$ need not be a positive definite self-adjoint linear map.

(b) (10 points) Prove that $\alpha ^ { 1 / 2 } \circ \beta \circ \alpha ^ { 1 / 2 } \colon V \to V$ is a positive definite self-adjoint linear map.

(c) (10 points) Prove that $\alpha \circ \beta$ is diagonalizable and that all its eigenvalues are positive and real.

[Hint: use the previous part.]

Total for Question 3: (25 points)

4. Here is the character table for a group G of size 168 with 1 of its rows missing (rows are characters, the columns are conjugacy classes):

<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>γ1</td><td rowspan=1 colspan=1>γ2</td><td rowspan=1 colspan=1>γ3</td><td rowspan=1 colspan=1>γ4</td><td rowspan=1 colspan=2>γ5</td><td rowspan=1 colspan=1>γ6</td></tr><tr><td rowspan=1 colspan=1>χ1X2</td><td rowspan=1 colspan=1>13</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>1-1-√-72</td><td rowspan=2 colspan=1>1-1+√-72</td><td rowspan=2 colspan=2>1−1−1</td><td rowspan=2 colspan=1>111</td></tr><tr><td rowspan=5 colspan=1>X3χ4X5X6</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>-1+√r7~</td></tr><tr><td rowspan=2 colspan=1>7</td><td rowspan=2 colspan=1>1</td><td rowspan=2 colspan=1>~</td><td rowspan=2 colspan=1>0</td><td rowspan=1 colspan=2>−1</td><td></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>−1</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=2>0</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=1>−1</td><td rowspan=1 colspan=1>?</td><td rowspan=1 colspan=2>?</td><td rowspan=1 colspan=1>0</td></tr></table>

The sizes of the conjugacy classes are $\left| \gamma _ { 1 } \right| = 1 , \left| \gamma _ { 2 } \right| = 5 6 , \left| \gamma _ { 3 } \right| = \left| \gamma _ { 4 } \right| = 2 4 , \left| \gamma _ { 5 } \right| = 2 1 , \left| \gamma _ { 6 } \right| = 4 2 .$

(a) (13 points) Fill in the correct values for $\chi _ { 6 }$

(b) (12 points) For $1 \leq i \leq 6 $ let $V _ { i }$ be a representation of G whose character is $\chi _ { i }$ . Compute the dimension of the space of G-equivariant linear maps from $V _ { 2 } \otimes V _ { 5 }$ to $V _ { 3 } \otimes V _ { 5 }$

Total for Question 4: (25 points)

5. Let the symmetric group ${ \mathfrak { S } } _ { 6 }$ act on the space of complex-coefficient homogeneous polynomials in $x _ { 1 } , \ldots , x _ { 6 }$ of degree 3 by substitution of variables.

Let V be the subspace spanned by $\{ x _ { i } x _ { j } x _ { k } \mid 1 \le i < j < k \le 6 \}$

(a) (10 points) What is the decomposition of V into irreducible representations?

(b) (15 points) Restrict V to ${ \mathfrak { S } } _ { 5 } \subset { \mathfrak { S } } _ { 6 }$ (the subgroup of permutations of $\{ 1 , 2 , 3 , 4 , 5 \} )$ . Write its character (explicitly, like a row in the previous problem).

Total for Question 5: (25 points)

6. Let $e _ { n }$ denote the n-th elementary symmetric polynomial.

(a) (13 points) Write $e _ { 4 } ( x _ { 1 } , x _ { 2 } , \ldots , x _ { 1 0 } , x _ { 1 } , x _ { 2 } , \ldots , x _ { 1 0 } )$ as a linear combination of Schur polynomials in $x _ { 1 } , \ldots , x _ { 1 0 }$

(b) (12 points) If we expand $s _ { 5 , 4 , 1 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } , 1 , 1 , 1 )$ into a linear combination of Schur polynomials, what is the coefficient of $s _ { 3 , 2 } ( x _ { 1 } , x _ { 2 } , x _ { 3 } ) ?$

Total for Question 6: (25 points)

7. (25 points) Let $R \colon { \mathrm { G } }  { \mathrm { G L } } ( { \mathcal { H } } )$ be a linear representation of a compact group G on a finitedimensional Hilbert space H. Prove that, for all $g \in \mathrm { G }$ , the eigenvalues of $R ( g )$ have modulus 1.

8. (25 points) Let $U \colon \mathrm { G } \to \mathrm { U } ( { \mathcal { H } } )$ be a unitary representation of a compact group G on a Hilbert space H. Prove that, if K is a closed subspace of H invariant under the action of G, so is $\kappa ^ { \perp }$

## End of Examination