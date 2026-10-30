# Applied Algebra Qualifying Exam, Fall 2022

Friday September 2 2022, 1:00 PM – 4:00 PM PDT.

• Complete the following problems, or as much of them as you can. There are eight problems carrying 25 points each. In order to receive full credit, please show all of your work and justify your answers. Partial answers may receive partial credit.

• You may use any result proved in lectures, a textbook, problem sets, or any other clearly referenced source; provided it is true, and unless (i) you are specifically instructed not to, or (ii) the result renders the question entirely trivial, e.g. because the question asks you to prove that result. You should state results clearly before using them.

• Insofar as it makes sense in context, you may answer later parts of a question (for full credit) without having correctly answered previous parts, and in your answer you may assume the conclusions of previous parts.

• You may not consult textbooks, your own notes, or any other source during the exam.

• In particular may not consult the internet—e.g., to search for or access online resources—during the exam.

• You may not seek assistance from other people during the exam (including electronically).

• You have 3 hours. When you are finished, please hand your completed script to the instructor.

• You should record your answers in the answer booklet provided. Please record your answers on the pages corresponding to each question. If you need more space, indicate clearly where the rest of your answer is to be found.

• Under all circumstances, remain calm.

1. A linear map $\phi \colon \mathbb { C } ^ { 1 0 } \to \mathbb { C } ^ { 1 0 }$ is given in the standard basis $e _ { 1 } , \ldots , e _ { 1 0 }$ by the matrix

$$
\left( \begin{array} { l l l l l l l l l l l } { 0 } & { 0 } & { * } & { * } & { * } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 1 } & { * } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 2 } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 3 } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 4 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 5 } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 6 } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 7 } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 8 } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 8 } \end{array} \right)
$$

where ∗ denotes an unknown value.

(a) (10 points) Prove that dim ker $\phi = 2$ and that $\phi ^ { 8 } ( e _ { 1 0 } ) \neq 0$

(b) (15 points) Hence, or otherwise, determine (with proof) the Jordan Normal Form of $\phi$

Total for Question 1: (25 points)

2. Let V be a finite-dimensional complex inner product space of dimension n, and $\phi \colon V \to V$ a linear map. Suppose that B is an orthonormal basis for V such that the matrix

$$
A = \mathcal { M } ( \phi , B , B ) = \left( \begin{array} { c c c c } { { \lambda _ { 1 } } } & { { \ast } } & { { \cdot \cdot } } & { { \ast } } \\ { { 0 } } & { { \lambda _ { 2 } } } & { { \cdot \cdot } } & { { \ast } } \\ { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { 0 } } & { { 0 } } & { { \cdot \cdot } } & { { \lambda _ { n } } } \end{array} \right)
$$

is upper-triangular, i.e., a Schur decomposition. Finally let $\sigma _ { 1 } \geq \cdots \geq \sigma _ { n }$ denote the singular values of $\phi ,$ with multiplicity.

(a) (15 points) By considering $\| \phi \| _ { \mathrm { F r o b } }$ , or otherwise, prove that $\begin{array} { r } { \sum _ { i = 1 } ^ { n } | \lambda _ { i } | ^ { 2 } \leq \sum _ { i = 1 } ^ { n } \sigma _ { i } ^ { 2 } } \end{array}$

(b) (10 points) Suppose now that $\begin{array} { r } { \sum _ { i = 1 } ^ { n } | \lambda _ { i } | ^ { 2 } = \sum _ { i = 1 } ^ { n } \sigma _ { i } ^ { 2 } } \end{array}$ . By considering A, or otherwise, prove that φ is normal.

Total for Question 2: (25 points)

3. (25 points) Let V and W be two finite-dimensional real inner product spaces, dim $V = \dim W = n$ and let $\phi \colon V \to W$ be a linear map.

Suppose there exists a vector $v _ { 0 } \in V , \| v _ { 0 } \| = 1$ , such that $\lVert \phi ( v _ { 0 } ) \rVert \leq 1 0 ^ { - 1 0 }$

Prove the following “approximate rank–nullity” statement: there exists a subspace $W ^ { \prime } \subseteq W$ with dim $W ^ { \prime } \leq n - 1$ , with the property that

$$
\forall v \in V , \ \lVert v \rVert \leq 1 : \ \exists w \in W ^ { \prime } : \lVert \phi ( v ) - w \rVert \leq 1 0 ^ { - 1 0 } .
$$

[Hint: you can use the singular value decomposition, or argue directly.]

Total for Question 3: (25 points)

4. (25 points) Let X be the set of triples $( i , j , k )$ of integers such that $i , j , k \in \{ 1 , \ldots , 1 0 \}$ with the diagonal action of the symmetric group $S _ { 1 0 } \colon$

$$
\sigma \cdot ( i , j , k ) = ( \sigma ( i ) , \sigma ( j ) , \sigma ( k ) ) .
$$

Let V be the corresponding permutation representation over the complex numbers. When decomposed into a sum of irreducible representations, which Specht modules appear in V and what are their multiplicities?

Total for Question 4: (25 points)

5. (25 points) Let s denote the Schur function. Express the product

$$
s _ { 2 , 1 , 1 } s _ { 2 , 2 , 1 }
$$

as a linear combination of Schur functions.

Total for Question 5: (25 points)

6. Let $G$ be a finite group and let V be a finite-dimensional complex representation of G with character $\chi .$ Consider the operator σ on $V \otimes V$ which swaps factors. Let $S ^ { 2 } ( V )$ be the subspace invariant under σ.

(a) (10 points) Show that $S ^ { 2 } ( V )$ is a G-subrepresentation of $V \otimes V$

(b) (15 points) Let $\chi _ { 2 }$ be the character of $S ^ { 2 } ( V )$ . Show that

$$
\chi _ { 2 } ( g ) = { \frac { 1 } { 2 } } ( \chi ( g ) ^ { 2 } + \chi ( g ^ { 2 } ) )
$$

for all $g \in G$ (the product in G is written as multiplication).

[Hint: Consider a basis of eigenvectors for g acting on V and use this to find a basis of eigenvectors for $S ^ { 2 } ( V ) .$ ]

Total for Question 6: (25 points)

7. (25 points) Show that any tensor $T \in \mathbb { C } ^ { 3 } \wedge \mathbb { C } ^ { 3 }$ can be written as ${ T = \mathbf { v } _ { 1 } \wedge \mathbf { v } _ { 2 } }$ for some $\mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } \in \mathbb { C } ^ { 3 }$

8. (25 points) Given a Young diagram $\alpha \vdash d ,$ identify the corresponding conjugacy class $C _ { \alpha } \subset$ $\mathrm { S } ( d )$ with the formal sum of its elements, so that it becomes an element of the group algebra $\mathbb { C } \mathrm { S } ( d )$ . Given another Young diagram $\lambda \vdash d ,$ show that $C _ { \alpha }$ acts in the corresponding irreducible representation $\mathbf { V } ^ { \lambda }$ of $\mathbb { C } \mathrm { S } ( d )$ as multiplication by a scalar $\omega _ { \alpha } ^ { \lambda } ,$ and compute this number in terms of the character of $\mathbf { V } ^ { \lambda }$ . Now, compute $\omega _ { \alpha } ^ { \lambda }$ explicitly in the case $\alpha = ( 2 1 ^ { d - 2 } )$ , corresponding to the conjugacy class of transpositions.

## End of Examination