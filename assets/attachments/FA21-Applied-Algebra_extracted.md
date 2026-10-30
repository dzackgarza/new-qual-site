# Fall Applied Algebra Qualifying Exam: Part A

5:00pm–8:00pm (PDT), via Zoom. Meeting ID: 943 0514 4675 Tuesday September 7th, 2021

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

– eig(A) is the set of eigenvalues of the matrix A (counting multiplicities).

– Re(α) is the real part of the complex scalar α.

– Im(α) is the imaginary part of the complex scalar α.

## Question 1.

(a) (3 points) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M _ { n }$

(b) (12 points) Prove that for A, $B \in \mathcal { M } _ { n }$ , if $x ^ { H } A x = x ^ { H } B x$ for all $x \in \mathbb { C } ^ { n }$ , then $A = B$ . Give an example for which $x ^ { T } A x = x ^ { T } B x$ for all $x \in \mathbb { C } ^ { n }$ but $A \neq B$

(c) (10 points) Prove that A is an orthogonal projection if and only if A is Hermitian, i.e., $A = A ^ { H }$

Question 2. Assume that the eigenvalues of a Hermitian matrix $A \in { \mathcal { M } } _ { n }$ are arranged in the order

$$
\lambda _ { n } ( A ) \leq \cdot \cdot \cdot \leq \lambda _ { 2 } ( A ) \leq \lambda _ { 1 } ( A ) .
$$

(a) (5 points.) Let $A \in { \mathcal { M } } _ { n }$ be Hermitian. Prove that

$$
\lambda _ { n } = \operatorname* { m i n } _ { x \neq 0 } { \frac { x ^ { H } A x } { x ^ { H } x } } .
$$

(b) (8 points) Prove that every $A \in \mathcal { M } _ { n }$ may be written uniquely as $A = S + i T$ where S and T are Hermitian.

(c) (12 points) For any $A \in { \mathcal { M } } _ { n }$ , consider the unique expansion $A = S + i T$ , where S and T are Hermitian. Prove that for any $\lambda \in \mathrm { e i g } ( A )$ , it holds that

$$
\lambda _ { n } ( S ) \leq \operatorname { R e } ( \lambda ) \leq \lambda _ { 1 } ( S ) \quad { \mathrm { a n d } } \quad \lambda _ { n } ( T ) \leq \operatorname { I m } ( \lambda ) \leq \lambda _ { 1 } ( T ) .
$$

## Question 3.

(a) (2 points) Define $A ^ { \frac { 1 } { 2 } }$ for a positive semidefinite $A \in \mathcal { M } _ { n }$

(b) (2 points) Define $| A |$ for any $A \in \mathcal { M } _ { m , n }$

(c) (7 points) Prove that the eigenvalues of |A| are the singular values of A.

(d) (7 points) Prove that A is positive semidefinite if and only ${ \mathrm { i f ~ } } | A | = A$

(e) (7 points) Prove that |A| and $| A ^ { H } |$ are similar.

## Question 4.

(a) (4 points.) Define the p-norm $\| A \| _ { p }$ and Frobenius norm $\| A \| _ { F }$ of a matrix $A \in \mathcal { M } _ { m , n } .$

(b) (6 points.) For every $A \in \mathcal { M } _ { m , n }$ , establish the following identities:

(i) $\| A ^ { H } \| _ { 2 } = \| A \| _ { 2 }$

(ii) $\| A ^ { H } A \| _ { 2 } = \| A ^ { H } \| _ { 2 } \| A \| _ { 2 }$

(c) (6 points.) Given two n-vectors x and y and the matrix $\boldsymbol { Z } = \boldsymbol { x } \boldsymbol { y } ^ { H }$ , show that

$$
\| Z \| _ { 2 } = \| Z \| _ { F } = \| x \| _ { 2 } \| y \| _ { 2 } .
$$

(d) (9 points.) Prove that the Frobenius norm and the matrix two-norm are invariant under unitary transformations, $\mathrm { i . e . }$ , show that if $P$ and $Q$ are unitary matrices of suitable dimension, then

$$
\| A \| _ { 2 } = \| P A Q \| _ { 2 } \mathrm { a n d } \| A \| _ { F } = \| P A Q \| _ { F } .
$$

## Applied Algebra Qualifying Exam: Part B Fall 2021

Instructions: Do all problems. All problems are weighted equally. You are not allowed to consult any external resource during this exam. Good luck!

Problem 1: Let G be a finite group and let V be an irreducible complex representation of G. If $g \in G$ lies in the center of $G ,$ show that there exists $c \in \mathbb { C }$ with

$$
g \cdot v = c v
$$

for all $v \in V$

Problem 2: Let Z be the additive group of integers. Is every indecomposable Z-module over the complex numbers irreducible?

Problem 3: Write down the character table of the symmetric group $S _ { 4 }$ . If we let

$$
X : = \{ { \mathrm { a l l ~ } } 2 { \mathrm { - e l e m e n t ~ s u b s e t s ~ o f ~ } } \{ 1 , 2 , 3 , 4 \} \}
$$

then $X$ carries a natural permutation action of $S _ { 4 }$ . Find the decomposition of C[X] into irreducibles.

Problem 4: Find the character table of the dihedral group $D _ { 4 }$ of symmetries of a square. The group algebra of $D _ { 4 }$ is isomorphic to a direct sum

$$
\mathbb { C } [ D _ { 4 } ] \cong \mathrm { M a t } _ { n _ { 1 } } ( \mathbb { C } ) \oplus \cdot \cdot \cdot \oplus \mathrm { M a t } _ { n _ { r } } ( \mathbb { C } )
$$

of matrix algebras over C. Determine r and the numbers $n _ { 1 } , \ldots , n _ { r } > 0$ . (Hint: Try showing that $\mathbb { C } [ D _ { 4 } ] \cong \operatorname { E n d } _ { D _ { 4 } } \mathbb { C } [ D _ { 4 } ]$ as algebras. How does the endomorphism ring of $\mathbb { C } [ D _ { 4 } ]$ decompose?)

# Applied Algebra Qualifying Exam: Part C

5:00pm–8:00pm (PDT), via Zoom. Tuesday September 7th, 2021

• Write your name and student PID at the top right corner of each page of your submission.

• Do both problems. Show your work.

• This part of the exam will represent 20% of the total score.

• Your completed examination must be uploaded to Gradescope while you are connected to Zoom. You may leave the meeting once the Proctor has checked that your exam has been uploaded.

• It is your responsibility to check that any uploaded material is both complete and legible.

• By participating in this exam you are agreeing to abide by the UCSD Policy on Academic Integrity. The instructors reserve the right to require a follow-up oral examination.

• This is a closed-book examination. No cell-phone or Internet aids.

• Please keep your camera turned on throughout the exam.

## Question 1.

(a) (2 points) Let $\mathrm { C } ( d )$ be the group generated by the cyclic permutation $\gamma =$ $( 1 2 \ldots d )$ in the symmetric group $\mathrm { S } ( d )$ . Explicitly describe the dual group of C(d).

(b) (8 points) State the definition of the Cayley graph of C(d), and find its eigenvalues and eigenvectors.

## Question 2. Let γ

(a) (2 points.) Given a Young diagram $\alpha \vdash d ,$ identity the corresponding conjugacy class $C _ { \alpha } \subset \mathrm { S } ( d )$ with the formal sum of its elements, so that it becomes an element of the group algebra $\mathbb { C } \mathrm { S } ( d )$ . Given another Young diagram $\lambda \vdash d ,$ show that $C _ { \alpha }$ acts in the corresponding irreducible representation $V ^ { \lambda }$ of $\mathbb { C } \mathrm { S } ( d )$ as multiplication by a scalar, $\omega _ { \alpha } ^ { \lambda }$ , and express this number in terms of the character of $V ^ { \lambda }$

(b) (8 points) Compute the $\omega _ { \alpha } ^ { \lambda }$ explicitly in the case that $\alpha = ( d )$ is the Young diagram consisting of a single row of d cells.