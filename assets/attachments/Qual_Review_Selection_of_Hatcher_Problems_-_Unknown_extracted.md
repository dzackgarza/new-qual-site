<!-- page 1 -->

Math 634–636, 2013–2014
Review sheet for the qualifying exam

Here are some practice problems to think about as you're preparing for the qualifying exam. You should add to this list all homework and exam problems from 634–636. These can be found at the three websites

http://math.uoregon.edu/~ddugger/ma634.html

http://math.uoregon.edu/~ddugger/ma635.html

http://math.uoregon.edu/~ddugger/ma636.html.

I would say that the homework and exam problems from this year are probably the most important things to make sure you understand. But it's useful to have other problems to practice on, to solidify your knowledge.

# Homology

You should know all the basic definitions and properties of singular, simplicial, and cellular homology. You should know the Zig-Zag Lemma, the Five Lemma, and other basic facts about homological algebra. You should be able to perform a range of calculations comparable to what we've done on homework assignments throughout the year, and reproduce basic proofs.

Problems from Hatcher:

- Section 2.1: 1, 2, 3, 4–7, 8, 9, 11, 12, 14, 17, 20, 22, 27, 28, 29, 31.
- Section 2.2: 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 19, 23, 27, 28, 29, 31, 32, 33, 34, 36, 40, 43a.
- Section 2.B: 8.

# Homotopy groups

You should be able to define higher homotopy groups and sketch proofs of their basic properties (the fact that they *are* groups, what happens when you change basepoint, etc). Know the definition of fiber bundle, the Homotopy Lifting Property, and the proof that a fiber bundle induces a long exact sequence of homotopy groups. Know the Cellular Approximation Theorem and what it's good for. Know Van Kampen's Theorem, the Hurewicz Theorem, and how to use them. Know the construction of Eilenberg-MacLane spaces.

Problems from Hatcher:

- Section 1.1: 1, 2, 5, 6, 8, 10, 13, 16.
- Section 1.2: 7, 8, 10, 11, 14, 15, 16, 21.
- Section 4.1: 1, 2.
- Section 4.2: 1, 2, 31, 32, 33.

# Covering spaces

Here you should know the basic classification theorem, and be able to work a variety of different examples. Know the construction of the universal covering space, and the right action of the fundamental group on this space. Know the left action of the fundamental group on the fibers of any covering space. Be able to work with these actions in several specific examples.

Problems from Hatcher:

- Section 1.3: 1, 2, 4, 5, 9, 10, 12, 13, 14, 16, 18, 20, 21, 26, 27.

<!-- page 2 -->

# Cohomology

Know the basic definitions and properties of cohomology groups—singular, simplicial, and cellular. Know the Universal Coefficient theorems and their proofs; in particular, know the definitions of Ext and Tor. Given a $\Delta$-complex, know how to determine explicit cocycles generating the cohomology groups, and how to decide if two cocycles represent the same cohomology class.

Know the definition of cup products, the basic properties, and how to compute them. Be familiar with many different applications. Know the Künneth Theorem, both for homology and cohomology.

Problems from Hatcher:

- Section 3.1: 1, 2, 6, 7, 8, 9.
- Section 3.2: 1, 3, 6, 7, 8, 11, 16, 18.
- Section 3.A: 3.
- Section 3.B: 1, 2.

# Manifolds and Poincaré Duality

Know the definition of a manifold being $R$-orientable, and how to translate this into a statement about covering spaces. Know the theorem that characterizes $R$-orientability of a compact $n$-manifold in terms of $H_n(-; R)$. Know the definition of fundamental class, and be able to construct fundamental classes in simple examples. Know the definition of cap product and be able to prove the basic properties. Know the definition of cohomology with compact support. Know the statements of Poincaré Duality, Lefschetz duality, and Alexander duality. Understand perfect pairings, how they arise in relation to Poincaré Duality, and how to make use of them. Know the Lefschetz Fixed Point Theorem.

Problems from Hatcher:

- Section 3.3: 2, 5, 7, 16, 20, 21, 25, 26.

Warning: When doing Mayer-Vietoris arguments, most of you have gotten pretty lax about saying exactly what the $U$ and $V$ are. Be more careful about this on the qualifying exam, as I will not be the only one grading it.

# More practice problems

1. Let $R$ be a ring. If $z = \sum_i r_i \sigma_i$ is a $k$-cycle in $C_k(X; R)$ (where $r_i \in R$ and $\sigma_i: \Delta^k \to X$), and $\alpha \in C^k(X; R)$, then define

$$\langle z, \alpha \rangle = \sum_i r_i \cdot \alpha(\sigma_i).$$

Prove that if $z - z'$ is a boundary, then $\langle z, \alpha \rangle = \langle z', \alpha \rangle$. Likewise, prove that if $\alpha$ is a coboundary and $z$ is a cycle then $\langle z, \alpha \rangle = 0$. Deduce that one gets a well-defined bilinear pairing of abelian groups

$$H_k(X; R) \times H^k(X; R) \to R.$$

This is sometimes called the Kronecker product.

2. Suppose $C_*$ and $D_*$ are bounded below chain complexes. One can form a double chain complex $\operatorname{Hom}(C_*, D_*)$ in the obvious way, having the group $\operatorname{Hom}(C_i, D_j)$ in spot $(i, j)$. Write $\underline{\operatorname{Hom}}(C_*, D_*)$ for the total complex of $\operatorname{Hom}(C_i, D_j)$. Here are several facts:

(i) If $C_*$ is free, then the functor $D_* \mapsto \underline{\operatorname{Hom}}(C_*, D_*)$ preserves all quasi-isomorphisms;
(ii) For any $D_*$, the functor $C_* \mapsto \underline{\operatorname{Hom}}(C_*, D_*)$ preserves chain homotopies.

Page 2

<!-- page 3 -->

Prove (ii).

If you are told that

$$H_{0}(C)=\mathbb{Z},\quad H_{1}(C)=\mathbb{Z}/3\oplus\mathbb{Z},\quad H_{2}(C)=\mathbb{Z}/4,\quad H_{3}(C)=\mathbb{Z}/2,$$

$$H_{0}(D)=\mathbb{Z}/8,\quad H_{1}(D)=\mathbb{Z}\oplus\mathbb{Z}/6,\quad H_{2}(D)=\mathbb{Z}/2,$$

and all other homology groups are zero, determine the homology groups of $\underline{\mathrm{Hom}}(C_{*},D_{*})$.

Use the same circle of ideas that we used when proving the Künneth Theorem.

3. (a) Let $X$ be a topological space with subspaces $A_{1},A_{2},\ldots,A_{n}$. Assume that each $A_{i}$ is contractible, and $\bigcup_{i}A_{i}=X$. Prove that if $R$ is a ring and one has elements $\alpha_{1},\ldots,\alpha_{n}\in H^{*}(X;R)$, all of positive degree, then the cup product $\alpha_{1}\cup\cdots\cup\alpha_{n}$ is zero.

(b) Prove that $\mathbb{R}P^{n}$ cannot be covered by $n$ contractible subspaces.

4. Let $f\colon S^{4}\to S^{4}$ be defined by

$$f(x,y,z,w)=\frac{1}{\sqrt{x^{4}+y^{4}+z^{4}+w^{4}}}(x^{2},y^{2},z^{2},w^{2}).$$

Compute the degree of $f$.

5. Compute the homology and cohomology groups of $\mathbb{R}P^{n}-\{x,y\}$, where $x$ and $y$ are distinct points in $\mathbb{R}P^{n}$.

6. The following picture depicts a 2-manifold $X$:

![img-0.jpeg](img-0.jpeg)

We know that every 2-manifold is homeomorphic to one of

$$S^{2},\ T_{1},\ T_{2},\ \ldots,\ \mathbb{R}P^{2},\ \mathbb{R}P^{2}\#\mathbb{R}P^{2},\ \mathbb{R}P^{2}\#\mathbb{R}P^{2}\#\mathbb{R}P^{2},\ \ldots$$

Determine which of these 2-manifolds is homeomorphic to $X$.

7. Repeat the above problem for the space $Y$ which is constructed similarly to $X$, but where two of the tori making up the "links" in the circular chain are replaced by $\mathbb{R}P^{2}$'s.

8. Determine whether each of the following statements is true or false, and give reasons:

(a) There exists a covering space \(S^2\to T\) (where \(T\) is the torus).
(b) There exists a covering space \(T\to S^2\)
(c) There exists a non-trivial covering space \(S^3\to S^3\)

9. Let $e$ be any point in $S^{n}$. Suppose that there is a map $\mu\colon S^{n}\times S^{n}\to S^{n}$ with the property that for all $x$ in $S^{n}$ one has $\mu(x,e)=x=\mu(e,x)$. Prove that $n$ must be odd. (In fact, $n$ must be 1, 3, or 7—but this stronger result is quite a bit harder).

Page 3

<!-- page 4 -->

10. Let $f: S^n \times S^n \to S^n \times S^n$ be a homeomorphism. Let $z$ be a generator for $H^n(S^n)$, and write $\alpha = z \times 1$ and $\beta = 1 \times z$ in $H^n(S^n \times S^n)$. We know these classes generate $H^n(S^n \times S^n)$, so we can write

$$f^*(\alpha) = k\alpha + l\beta, \qquad f^*(\beta) = p\alpha + q\beta$$

for some $k, l, p, q \in \mathbb{Z}$. Prove that if $n$ is even then the matrix $\begin{pmatrix} k & l \\ p & q \end{pmatrix}$ must be one of the following eight possibilities:

$$\begin{pmatrix} \pm 1 & 0 \\ 0 & \pm 1 \end{pmatrix}, \qquad \begin{pmatrix} \pm 1 & 0 \\ 0 & \mp 1 \end{pmatrix}, \qquad \begin{pmatrix} 0 & \pm 1 \\ \pm 1 & 0 \end{pmatrix}, \qquad \begin{pmatrix} 0 & \pm 1 \\ \mp 1 & 0 \end{pmatrix}.$$

Also, find homeomorphisms $f$ showing that the above eight matrices really do occur.

11. Find a subgroup $\Gamma \subseteq \operatorname{Aut}(\mathbb{R}^2)$ such that $\mathbb{R}^2/\Gamma$ is homeomorphic to the Klein bottle. Recall that if $G$ is a group acting on a topological space $X$, then $X/G$ denotes the quotient space $X/\sim$ where the equivalence relation has $x \sim gx$ for every $x \in X$ and $g \in G$.
12. Let $M$ be an $n$-manifold. Prove that $M$ is not a $k$-manifold for any $k \neq n$.
13. Prove that $S^1 \vee S^1$ is not a retract of $S^1 \times S^1$.
14. Let $n \ge 2$. Prove that there does not exist an integer $k$ and a space $X$ such that $\mathbb{C}P^n \simeq S^k \vee X$.
15. Suppose that $X$ and $Y$ are spaces such that $X \times Y \simeq \mathbb{C}P^n$, $n \ge 1$. Prove that either $H^i(X) = 0$ for all $i > 0$, or else $H^i(Y) = 0$ for all $i > 0$.
16. Let $f \in \mathbb{C}[z]$ and assume $f$ has no roots on the unit circle. Consider the composition

$$S^1 \in \mathbb{C} \xrightarrow{f} \mathbb{C} - \{0\} \xrightarrow{\pi} S^1$$

where $\pi$ is the norm map. Prove that the degree of this composition is equal to the number of roots of $f$ that lie inside the unit circle.

Page 4
