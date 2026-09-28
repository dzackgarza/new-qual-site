---
schema: qual/card@1
id: P-BKF80-6
kind: problem
title: Complex subrings of $M_2(\mathbb R)$ and a matrix polynomial equation
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $M_2(\RR)$ be the ring of real $2\times2$ matrices, and let
$$
S=\left\{
\begin{pmatrix}a&-b\\ b&a\end{pmatrix}:a,b\in\RR
\right\}.
$$

1. Exhibit an isomorphism $S\cong\CC$.
2. Prove that
$$
A=\begin{pmatrix}0&3\\-4&1\end{pmatrix}
$$
lies in a subring of $M_2(\RR)$ isomorphic to $S$.
3. Prove that there exists $X\in M_2(\RR)$ such that
$$
X^4+13X=A.
$$
:::

::: {.solution}
<1>1. The map
$$
\Phi:\CC\longrightarrow S,
\qquad
\Phi(a+bi)=\begin{pmatrix}a&-b\\b&a\end{pmatrix},
$$
is a ring isomorphism.

::: {.proof}
The map is bijective by the definition of $S$. It preserves addition entrywise. For $z=a+bi$ and $w=c+di$,
$$
\Phi(z)\Phi(w)
=\begin{pmatrix}
ac-bd&-(ad+bc)\\
ad+bc&ac-bd
\end{pmatrix}
=\Phi(zw).
$$
Also $\Phi(1)=I_2$. Thus $\Phi$ is a ring isomorphism.
:::

<1>2. For
$$
J\coloneqq\frac{2A-I_2}{\sqrt{47}},
$$
one has $J^2=-I_2$.

::: {.proof}
The characteristic polynomial of $A$ is
$$
\chi_A(T)=T^2-T+12.
$$
By the Cayley--Hamilton theorem,
$$
A^2-A+12I_2=0.
$$
Therefore
$$
J^2
=\frac{4A^2-4A+I_2}{47}
=\frac{4(A-12I_2)-4A+I_2}{47}
=-I_2.
$$
:::

<1>3. The set
$$
T\coloneqq\{aI_2+bJ:a,b\in\RR\}
$$
is a subring of $M_2(\RR)$ isomorphic to $S$, and $A\in T$.

::: {.proof}
Because $J^2=-I_2$ by step <1>2, the map
$$
\Psi:\CC\longrightarrow T,
\qquad
\Psi(a+bi)=aI_2+bJ,
$$
preserves addition and multiplication. It is surjective by definition. If
$$
aI_2+bJ=0,
$$
and $b\neq0$, then $J=-(a/b)I_2$, whose square is a nonnegative scalar multiple of $I_2$, contradicting $J^2=-I_2$. Thus $b=0$, and then $a=0$, so $\Psi$ is injective. Hence $T\cong\CC$, and step <1>1 gives $T\cong S$.

Finally, the definition of $J$ rearranges to
$$
A=\frac12I_2+\frac{\sqrt{47}}2J,
$$
so $A\in T$.
:::

<1>4. There exists $X\in M_2(\RR)$ satisfying $X^4+13X=A$.

::: {.proof}
Under the isomorphism $\Psi$ of step <1>3, the matrix $A$ corresponds to
$$
\alpha\coloneqq\frac12+\frac{\sqrt{47}}2i\in\CC.
$$
By the fundamental theorem of algebra, the polynomial
$$
p(z)=z^4+13z-\alpha
$$
has a root $z_0\in\CC$. Set
$$
X\coloneqq\Psi(z_0)\in T\subset M_2(\RR).
$$
Since $\Psi$ is a ring homomorphism,
$$
X^4+13X
=\Psi(z_0^4+13z_0)
=\Psi(\alpha)
=A.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves part 1, step <1>3 proves part 2, and step <1>4 proves part 3.
:::
:::
