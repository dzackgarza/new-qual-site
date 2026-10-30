# Applied Algebra Qualifying Exam, Spring 2022

Monday May 16 2022, 5:00 PM – 8:00 PM PDT.

• Complete the following problems, or as much of them as you can. There are eight problems carrying 25 points each. In order to receive full credit, please show all of your work and justify your answers. Partial answers may receive partial credit.

• You may use any result proved in lectures, a textbook, problem sets, or any other clearly referenced source; provided it is true, and unless (i) you are specifically instructed not to, or (ii) the result renders the question entirely trivial, e.g. because the question asks you to prove that result. You should state results clearly before using them.

• Insofar as it makes sense in context, you may answer later parts of a question (for full credit) without having correctly answered previous parts, and in your answer you may assume the conclusions of previous parts.

• You may not consult textbooks, your own notes, or any other source during the exam.

• In particular may not consult the internet—e.g., to search for or access online resources—during the exam.

• You may not seek assistance from other people during the exam (including electronically).

• You have 3 hours. When you are finished, please hand your completed script to the instructor.

• You should record your answers in the answer booklet provided. Please record your answers on the pages corresponding to each question. If you need more space, indicate clearly where the rest of your answer is to be found.

• Under all circumstances, remain calm.

1. (25 points) A linear map $\phi \colon \mathbb { C } ^ { 7 } \to \mathbb { C } ^ { 7 }$ is given. It has the following properties.

• There exist two different bases $B _ { 1 }$ and $B _ { 2 }$ for $\mathbb { C } ^ { 7 }$ , such that the matrices of $\phi$ with respect to these bases are

$$
\mathcal { M } ( \phi , B _ { 1 } , B _ { 1 } ) = \left( \begin{array} { l l l l l l l } { 1 } & { 1 } & { 0 } & { * } & { * } & { * } \\ { - 1 } & { - 1 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \end{array} \right) , \mathcal { M } ( \phi , B _ { 2 } , B _ { 2 } ) = \left( \begin{array} { l l l l l l l } { 0 } & { * } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { * } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 1 } & { * } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { * } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { * } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 7 } \end{array} \right)
$$

where ∗ denotes an unknown value.

• We have dim ker $\left( \phi - \operatorname { i d } _ { \mathbb { C } ^ { 7 } } \right) = 1$

Determine, with proof, the Jordan Normal Form of $\phi .$

2. Let V be a finite-dimensional inner product space and write n = dim $V .$ . For the purposes of this question, the definition of a linear map $\phi \colon V  V$ being unitary is that $\phi$ is invertible and $\phi ^ { - 1 } = \phi ^ { * }$ (where $\phi ^ { * }$ is the adjoint of $\phi )$

(a) (8 points) Let $\phi \colon V \to V$ be a linear map, and write $\sigma _ { 1 } , \ldots , \sigma _ { n }$ for its singular values.

Prove that $\phi \colon V  V$ is unitary if and only if $\sigma _ { i } = 1$ for all $1 \leq i \leq n$

Now let $W = \mathbb { C } ^ { 1 0 0 }$ , considered as an inner product space with its usual inner product $( \mathrm { i . e . , }$ dot product).

(b) (17 points) Suppose $\psi \colon W \to W$ is a linear map such that $\mathrm { ( a ) } \parallel \psi \parallel _ { \mathrm { F r o b } } = 3 0$ , and $( \mathrm { b } ) \ \| \psi \| _ { \mathrm { o p } } \leq$ 3, where $\| \psi \| _ { \mathrm { o p } }$ denotes the operator norm with respect to the usual \`2-norm on $W$

Using (a), or otherwise, prove that $\psi$ is diagonalizable.

Total for Question 2: (25 points)

3. Let V be a finite-dimensional inner product space and $\alpha , \beta \colon V \to V$ two positive definite, selfadjoint linear maps. Define

$$
\langle v , w \rangle _ { \alpha } : = \langle \alpha ( v ) , w \rangle
$$

$$
\langle v , w \rangle _ { \beta } : = \langle \beta ( v ) , w \rangle
$$

to be the two new inner products on V associated with α and $\beta$ respectively.

(a) (8 points) If $\theta \colon V  V$ is a linear map, and $\theta ^ { * }$ denotes its adjoint with respect to the original inner product $\langle - , - \rangle$ on V , prove that the adjoint of θ with respect to the new inner product $\langle - , - \rangle _ { \alpha }$ is given by $\alpha ^ { - 1 } \theta ^ { \ast } \alpha$

(b) (2 points) Prove that the linear map $\gamma = \alpha ^ { - 1 } \beta$ is self-adjoint with respect to the new inner product $\langle - , - \rangle _ { \alpha }$

(c) (15 points) By applying a spectral theorem to $\langle - , - \rangle _ { \alpha }$ and $\gamma ,$ or otherwise, prove that there exists a basis $B = v _ { 1 } , \ldots , v _ { n }$ for V that is orthogonal with respect to both $\langle - , - \rangle _ { c }$ α and $\langle - , - \rangle _ { \beta }$ . (That is, $\langle \alpha ( v _ { i } ) , v _ { j } \rangle = \langle \beta ( v _ { i } ) , v _ { j } \rangle = 0 { \mathrm { ~ f o r ~ } } 1 \leq i \neq j \leq n . )$

Total for Question 3: (25 points)

4. Let G be the group of order 16 which is generated by 2 elements a, b that satisfy the relations (e is the identity)

$$
a ^ { 8 } = e , \quad b ^ { 2 } = e , \quad b a b ^ { - 1 } = a ^ { 5 } .
$$

(Any other relation is a consequence of these relations, i.e., we have described a presentation of G.)

(a) (15 points) Describe all of the 1-dimensional irreducible complex representations of G.

(b) (10 points) How many irreducible complex representations does G have and what are their dimensions?

Total for Question 4: (25 points)

5. Let $M _ { n }$ be the set of perfect matchings of $\{ 1 , 2 , \ldots , 2 n \}$ , i.e., a decomposition of this set into disjoint 2-element subsets. The permutation action of ${ \mathfrak { S } } _ { 2 n }$ induces an action on $M _ { n }$ . Let k be a field.

(a) (10 points) Describe a subgroup H of ${ \mathfrak { S } } _ { 2 n }$ so that the permutation representation $k [ M _ { n } ]$ is isomorphic to the induced representation of the trivial representation of H to ${ \mathfrak { S } } _ { 2 n }$

(b) (15 points) Construct a surjective ${ \mathfrak { S } } _ { 2 n }$ -equivariant map φ from $k [ M _ { n } ]$ onto the Specht module $\dot { \mathbf { S } } ^ { ( n , n ) }$ and describe a spanning set for the kernel of $\phi .$

[Note: This is very closely related to a homework problem. Do not use the result of that problem unless you are planning to reprove it.]

Total for Question 5: (25 points)

6. (a) (15 points) Let s denote the Schur symmetric functions, and let h, i denote the usual scalar product on the ring of symmetric functions. Compute

$$
{ \big \langle } s _ { ( 4 , 4 , 2 , 2 ) / ( 2 , 1 ) } , s _ { ( 4 , 3 , 2 , 2 ) / ( 1 , 1 ) } { \big \rangle } .
$$

(b) (10 points) What is the number of standard Young tableaux of shape (5, 3, 2, 2, 1)?

Total for Question 6: (25 points)

7. (25 points) Let $( \mathbf { S } ^ { \lambda } , \rho ^ { \lambda } )$ be the irreducible representation of the complex group algebra of the symmetric group ${ \mathfrak { S } } _ { 7 }$ corresponding to the partition $\lambda = ( 4 , 2 , 1 )$ . Using Murphy’s theorem (or otherwise), determine the spectrum of $\rho ^ { \lambda } ( T )$ , where T is the sum of all transpositions.

8. (25 points) Let $\left\{ \mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \mathbf { v } _ { 3 } , \mathbf { v } _ { 4 } \right\}$ be a linearly independent set in a C-vector space V. Prove that the tensor $\boldsymbol { \omega } = \mathbf { v } _ { 1 } \wedge \mathbf { v } _ { 2 } + \mathbf { v } _ { 3 } \wedge \mathbf { v } _ { 4 }$ cannot be represented as a single-term exterior product.

## End of Examination