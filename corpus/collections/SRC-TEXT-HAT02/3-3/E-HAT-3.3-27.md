---
schema: qual/card@1
id: E-HAT-3.3-27
kind: problem
title: Normal form for skew-symmetric forms over $\ZZ$
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 27; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 27; it matches the printed text. The printed bracketed hint about realizing row and column operations by a change of basis was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the induction: a primitive $e$ has $B(e,-)$ primitive, so some $f$ pairs to $1$; the
    symplectic correction $x'=x-B(x,f)e+B(x,e)f$ lies in $P^\perp$, which gives the orthogonal
    splitting $L=P\oplus P^\perp$ and lets the rank drop by two; replacing $f$ by $-f$ puts the
    block in the printed shape.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Filled two previously asserted steps in the integral normal-form proof. Nonsingularity and
    primitivity of e make B(e,-) a primitive functional, hence B(e,f)=1 for some f. The displayed
    correction gives both orthogonality equations, and the orthogonal splitting makes the
    restriction to P-perp nonsingular, permitting induction. D.G. James, Witt's Theorem for
    Symplectic Modular Forms, p.410, gives the same binary decomposition and confirms that a
    primitive vector can begin a symplectic basis.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Recomputed B(x',e)=B(x',f)=0 explicitly and checked the P-perp adjoint by extending any
    functional on P-perp by zero on P and using L=P plus P-perp. STYLE-08 conversion leaves the
    mathematics and the printed block unchanged.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Read Bourbaki, Algebre IX, section 5, no.1, theorem 1, printed pp.79-80, from the retained
    scan. Compared its induction with the card: the adjoint image and largest invariant factor
    produce the first binary summand, its orthogonal complement frees the next induction, and
    unimodularity over Z makes each invariant factor a unit. Added this complete published
    argument and its specialization to the exercise; James remains only a secondary pointer.
    Also corrected the primitive-functional factorization test to exclude only |m|>1, since
    m=+1 or -1 does not contradict primitivity.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Verified the Bourbaki citation and page range against the rendered pp.80-81 and the theorem
    beginning on p.79; the source is section 5, not section 4. Rechecked that applying the inverse
    adjoint to B-flat(e)=m lambda gives e=m times a lattice element, so exactly |m|>1 supplies the
    contradiction. The source theorem is stronger than the exercise and its displayed invariant-
    factor induction was compared with all three displayed steps, not merely cited by name.
---

::: {.problem}
Show that after a suitable change of basis, a skew-symmetric nonsingular bilinear form over $\ZZ$ can be represented by a matrix consisting of $2 \times 2$ blocks $\bigl(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\bigr)$ along the diagonal and zeros elsewhere.
[For the matrix of a bilinear form, the following operation can be realized by a change of basis: Add an integer multiple of the $i$th row to the $j$th row and add the same integer multiple of the $i$th column to the $j$th column. Use this to fix up each column in turn. Note that a skew-symmetric matrix must have zeros on the diagonal.]
:::

::: {.solution}
Let $L$ be a free abelian group of finite rank with a skew-symmetric nonsingular bilinear form
$$
B:L\times L\to\ZZ.
$$
Nonsingularity over $\ZZ$ means the adjoint map $L\to L^*$ is an isomorphism.

A complete published proof in greater generality is **N. Bourbaki, *Algèbre*, chapitre IX, §5, no. 1, théorème 1, printed pp. 79--80** (`tmp/sources/bourbaki-algebra-ch9-1959.pdf`). Its induction on rank uses the largest invariant factor of the image of the adjoint, splits off a two-dimensional orthogonal summand, and repeats on its orthogonal complement. For $A=\ZZ$ it gives $B(e_{2i-1},e_{2i})=\alpha_i$ with all other pairings zero. Nonsingularity makes the adjoint surjective, so the largest invariant factor at each stage is all of $\ZZ$; hence every $\alpha_i$ is $\pm1$, and changing the sign of every second basis vector where necessary gives the required blocks. **D. G. James, *Witt's Theorem for Symplectic Modular Forms*, p. 410** (`tmp/sources/james-witt-symplectic-modular-forms-1967.pdf`) states this integral decomposition and cites Bourbaki, but does not reproduce its induction. The following is the same splitting argument specialized to the unimodular integral case, with the primitive-functional step made explicit.

::: pf

::: {.pf-step #primitive-pair}
Every primitive $e\in L$ has a partner $f\in L$ with $B(e,f)=1$.

::: pf-proof
Let $B^\flat:L\to L^*$ be the adjoint isomorphism. If $B^\flat(e)=m\lambda$ for some $\lambda\in L^*$ and an integer $|m|>1$, then applying $(B^\flat)^{-1}$ shows that $e$ is $m$ times an element of $L$, contradicting primitivity of $e$. The cases $m=0$ and $m=\pm1$ are harmless. Thus $B^\flat(e)$ is primitive in $L^*$. A primitive functional is not an integer multiple of another functional with larger content, so its values include $1$: some $f\in L$ has $B(e,f)=1$.
:::

:::

::: {.pf-step #orthogonal-splitting}
For $P=\ZZ e\oplus\ZZ f$ we have $L=P\oplus P^\perp$, and $B$ has matrix
$$
\begin{pmatrix}0&1\\-1&0\end{pmatrix}
$$
on $P$.

::: pf-proof
For any $x\in L$, set
$$
x'=x-B(x,f)e+B(x,e)f.
$$
Then
$$
\begin{aligned}
B(x',e)&=B(x,e)-B(x,f)B(e,e)+B(x,e)B(f,e)=0,\\
B(x',f)&=B(x,f)-B(x,f)B(e,f)+B(x,e)B(f,f)=0.
\end{aligned}
$$
Thus $x'\in P^\perp$, and the first two terms in the formula for $x$ give the component of $x$ in $P$. The matrix on $P$ has determinant $1$, so $P\cap P^\perp=0$. Hence $L=P\oplus P^\perp$.
:::

:::

::: {.pf-step #restriction-nonsingular}
The restriction of $B$ to $P^\perp$ is integral, skew-symmetric, and nonsingular.

::: pf-proof
It is integral and skew-symmetric by restriction. Given $\varphi\in(P^\perp)^*$, extend it by zero on $P$. Nonsingularity of $B$ on $L$ gives $y\in L$ with $B(y,x)=\varphi(x)$ for every $x\in P^\perp$. Writing $y=p+z$ with $p\in P$ and $z\in P^\perp$ from step [](#orthogonal-splitting){.pf-ref} shows that $B(z,x)=\varphi(x)$ for all $x\in P^\perp$, so the restriction's adjoint is surjective. It is injective since $z\in P^\perp\cap(P^\perp)^\perp$ forces $z=0$ using the same decomposition for the zero functional.
:::

:::

::: pf-step
Induction on rank now gives the required block-diagonal matrix.

::: pf-proof
Starting with a primitive $e$, steps [](#primitive-pair){.pf-ref}–[](#restriction-nonsingular){.pf-ref} split off a rank-two symplectic plane, and step [](#restriction-nonsingular){.pf-ref} permits repetition on $P^\perp$. Induction ends with an orthogonal direct sum of these planes. Replacing $f$ by $-f$ in each plane changes each block to
$$
\boxed{\begin{pmatrix}0&-1\\1&0\end{pmatrix}},
$$
as required.
:::

:::

:::
:::
