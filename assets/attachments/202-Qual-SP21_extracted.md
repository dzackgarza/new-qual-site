# Applied Algebra Qualifying Exam: Part A

5:00pm–8:00pm (PDT), via Zoom. Meeting ID: 912 8480 3260 Tuesday May 11th, 2021

• Write your name and student PID at the top right corner of each page of your submission.

• Do all four problems. Show your work.

• This part of the exam will represent 40% of the total score.

• Your completed examination must be uploaded to Gradescope while you are connected to Zoom. You may leave the meeting once the Proctor has checked that your exam has been uploaded.

• It is your responsibility to check that any uploaded material is both complete and legible.

• By participating in this exam you are agreeing to abide by the UCSD Policy on Academic Integrity. The instructors reserve the right to require a follow-up oral examination.

• This is a closed-book examination. No cell-phone or Internet aids.

• Please keep your camera turned on throughout the exam.

• Notation:

$\mathcal { M } _ { m , n }$ denotes the set of $m \times n$ matrices with complex components.

$\mathcal { M } _ { n }$ denotes the set $\mathcal { M } _ { m , n }$ with $m = n$

$\mathbb { C } ^ { n }$ is the set of column vectors with n complex components.

$x ^ { H }$ is the Hermitian transpose of a vector or matrix x.

$- \ \mathrm { e i g } ( A )$ is the set of eigenvalues of the matrix A (counting multiplicities).

## Question 1.

(a) (4 points) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M _ { n }$

(b) (8 points) Let $( \lambda , x )$ be a simple eigenpair of $A \in M _ { n }$ with $x ^ { H } x = 1$ . Prove that there exists a nonsingular matrix $( \boldsymbol { x } \ : \boldsymbol { X } )$ with inverse $\left( \begin{array} { l l } { \boldsymbol { y } } & { \boldsymbol { Y } } \end{array} \right) ^ { H }$ such that

$$
\left( \begin{array} { c } { { y ^ { H } } } \\ { { Y ^ { H } } } \end{array} \right) A \left( \begin{array} { c c } { { x } } & { { X } } \end{array} \right) = \left( \begin{array} { c c } { { \lambda } } & { { 0 } } \\ { { 0 } } & { { M } } \end{array} \right) .
$$

(c) (8 points) Hence prove that the angle θ between x and y satisfies sec $\theta = \| y \| _ { 2 }$

## Question 2.

(a) (8 points.) Consider any Hermitian $A \in \mathcal { M } _ { n }$ with eigenvalues ordered so that $\lambda _ { n } ( A ) \leq \cdots \leq \lambda _ { 2 } ( A ) \leq \lambda _ { 1 } ( A )$ . Prove that

$$
\lambda _ { n } = \operatorname* { m i n } _ { x \neq 0 } { \frac { x ^ { H } A x } { x ^ { H } x } } .
$$

(b) (12 points) Suppose that $D \in \mathcal { M } _ { n }$ with $D = \operatorname { d i a g } ( d _ { 1 } , d _ { 2 } , \dotsc , d _ { n } )$ . Prove that for all $1 \leq p \leq \infty$ the p-norm of D is given by $\lVert D \rVert _ { p } = \operatorname* { m a x } _ { 1 \leq i \leq n } \left| d _ { i } \right|$

## Question 3.

(a) (4 points.) State, but do not prove, the singular-value decomposition theorem.

(b) (8 points.) For a given $A \in \mathcal { M } _ { m , n } ,$ prove that

$$
\sigma _ { 1 } ( A ) = \operatorname* { m a x } _ { \boldsymbol { x } , \boldsymbol { y } \neq \boldsymbol { 0 } } \frac { | \boldsymbol { y } ^ { H } \boldsymbol { A } \boldsymbol { x } | } { \| \boldsymbol { y } \| _ { 2 } \| \boldsymbol { x } \| _ { 2 } } ,
$$

where $\sigma _ { 1 } ( A )$ is the largest singular value of A.

(c) (8 points.) For any $A \in { \mathcal { M } } _ { n } ,$ , define (i) the field of values ${ \mathcal { F } } ( A ) ; ( { \mathrm { i i } } )$ the spectral radius $\rho ( A )$ ; and the numerical radius $\omega ( A )$ . Prove that $\rho ( A ) \leq \omega ( A ) \leq \sigma _ { 1 } ( A )$

## Question 4.

(a) (8 points) Let $C \in \mathcal { M } _ { m , n }$ with $\operatorname { r a n k } ( C ) = m$ Find orthogonal projections that project $x \in \mathbb { C } ^ { n }$ onto $\mathrm { r a n g e } ( C ^ { H } )$ and null(C). Verify that your projections satisfy the properties of an orthogonal projection.

(b) For a given nonzero $y \in \mathbb { C } ^ { n }$ , let $\mathcal { Y } = \operatorname { s p a n } ( y )$

(i) (6 points) Find an oblique projector A that project vectors onto $\mathcal { V } .$ Find the complementary projection.

(ii) (6 points) Find the unique orthogonal projector A that projects vectors onto $\mathcal { V } .$ Find the complementary projection associated with A.

## Applied Algebra Qualifying Exam: Part B Spring 2021

Instructions: Do all problems. All problems are weighted equally. You are not allowed to consult any external resource during this exam. Good luck!

Problem 1: Let G be a group (possibly infinite) and let V be a finite-dimensional G-module over C. Assume that V admits a G-invariant inner product h−, −i. Prove that V is completely reducible.

Problem 2: Let $\mathbb { R } _ { + }$ be the group of positive real numbers under multiplication. Is every indecomposable R+-module over the complex numbers irreducible?

Problem 3: Let $\lambda , \mu \vdash n$ be partitions and let $S ^ { \lambda } , S ^ { \mu }$ be the corresponding irreducible $S _ { n ^ { - } } { \mathrm { m o d u l e s } }$ . Endow the tensor product $S ^ { \lambda } \otimes S ^ { \mu }$ with the structure of an $S _ { n ^ { - } } { \mathrm { m o d u l e } }$ by the rule

$$
\sigma \cdot ( v \otimes w ) : = ( \sigma \cdot v ) \otimes ( \sigma \cdot w )
$$

for $\sigma \in S _ { n } , v \in S ^ { \lambda } , w \in S ^ { \mu }$ . Find the vector space dimension of the $S _ { n }$ -fixed subspace

$$
( S ^ { \lambda } \otimes S ^ { \mu } ) ^ { S _ { n } }
$$

of $S ^ { \lambda } \otimes S ^ { \mu }$

Problem 4: Find the character table of the alternating subgroup $A _ { 4 }$ of the symmetric group $S _ { 4 }$ . The group algebra of $A _ { 4 }$ is isomorphic to a direct sum

$$
\mathbb { C } [ A _ { 4 } ] \cong \mathrm { M a t } _ { n _ { 1 } } ( \mathbb { C } ) \oplus \dots \oplus \mathrm { M a t } _ { n _ { r } } ( \mathbb { C } )
$$

of matrix algebras over C. Determine r and the numbers $n _ { 1 } , \ldots , n _ { r } > 0$

# Applied Algebra Qualifying Exam: Part C

5:00pm–8:00pm (PDT), via Zoom. Meeting ID: 912 8480 3260 Tuesday May 11th, 2021

• Write your name and student PID at the top right corner of each page of your submission.

• Do both problems. Show your work.

• This part of the exam will represent 20% of the total score.

• Your completed examination must be uploaded to Gradescope while you are connected to Zoom. You may leave the meeting once the Proctor has checked that your exam has been uploaded.

• It is your responsibility to check that any uploaded material is both complete and legible.

• By participating in this exam you are agreeing to abide by the UCSD Policy on Academic Integrity. The instructors reserve the right to require a follow-up oral examination.

• This is a closed-book examination. No cell-phone or Internet aids.

• Please keep your camera turned on throughout the exam.

## Question 1.

(a) (2 points) Let $\mathrm { B } ( n )$ be the permutation group generated by the transpositions $\tau _ { i } = ( 2 i - 1 2 i )$ 2 $1 \leq i \leq n$ . Show that every character $\chi$ of $\mathrm { B } ( n )$ takes values in $\{ - 1 , 1 \}$

(b) (8 points) Explicitly describe the dual group of B(n).

## Question 2.

(a) (2 points.) With notation as in the previous problem, give the definition of the Cayley graph of $\mathrm { B } ( n )$ as generated by τ1, . . . , τn.

(b) (8 points) Compute the eigenvalues and eigenvectors of the adjacency operator of the graph in part (a).