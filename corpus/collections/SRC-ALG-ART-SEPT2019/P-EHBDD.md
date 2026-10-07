---
schema: qual/card@1
id: P-EHBDD
kind: problem
title: Semisimplicity and the Jacobson radical of the corner ring $eRe$
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Jacobson Radical
  - Rings
relations: []
review: draft
---

::: {.problem}
In this question, $R$ is a ring and $e \in R$ is an idempotent, so that $eRe$ is another ring with identity element $e$.

a. What does it mean to say that $R$ is *semisimple*? State the Artin-Wedderburn Theorem.
b. If $V$ is a completely reducible $R$-module of finite length, show that the algebra $\operatorname{End}_R(V)$ is semisimple.
Deduce for a semisimple ring $R$ that $eRe$ is semisimple too.
c. Assuming that $R$ is left Artinian, show that $J(eRe) = eJ(R)e$, where $J$ denotes Jacobson radical.
:::

::: {.solution}
<1>1. A ring $R$ is semisimple exactly when the left regular module ${}_RR$ is completely reducible; equivalently,
$$
\boxed{R\cong\prod_{i=1}^r M_{n_i}(D_i)}
$$
for division rings $D_i$ and positive integers $n_i$.
::: {.proof}
This is the Artin--Wedderburn theorem.
:::

<1>2. If $V$ is a completely reducible $R$-module of finite length, then $\End_R(V)$ is semisimple.
::: {.proof}
Write
$$
V\cong L_1^{\oplus n_1}\oplus\cdots\oplus L_r^{\oplus n_r},
$$
where the $L_i$ are pairwise nonisomorphic simple $R$-modules. By Schur's lemma,
$$
D_i\coloneqq\End_R(L_i)
$$
is a division ring, and
$$
\Hom_R(L_i,L_j)=0\qquad(i\ne j).
$$
Hence
$$
\End_R(V)
\cong
\prod_{i=1}^r M_{n_i}(D_i),
$$
which is semisimple by step <1>1.
:::

<1>3. If $R$ is semisimple and $e^2=e$, then
$$
\boxed{eRe\text{ is semisimple}}.
$$
::: {.proof}
The left ideal $Re$ is a direct summand of ${}_RR$, hence is completely reducible of finite length. Right multiplication gives an anti-isomorphism
$$
eRe\xrightarrow{\sim}\End_R(Re),
$$
equivalently
$$
eRe\cong\End_R(Re)^{\op}.
$$
By step <1>2, $\End_R(Re)$ is semisimple, and the opposite ring of a semisimple ring is semisimple. Therefore $eRe$ is semisimple.
:::

<1>4. If $R$ is left Artinian, then $eRe$ is left Artinian.
::: {.proof}
Let
$$
I_1\supseteq I_2\supseteq\cdots
$$
be a descending chain of left ideals of $eRe$. Then
$$
RI_1\supseteq RI_2\supseteq\cdots
$$
is a descending chain of left ideals of $R$, so it stabilizes. Multiplying by $e$ on the left gives stabilization of
$$
eRI_j.
$$
For every left ideal $I\subseteq eRe$,
$$
eRI=eReI=I,
$$
because each $i\in I$ satisfies $i=ei$. Hence the original chain stabilizes.
:::

<1>5. The ideal $eJ(R)e$ is a nilpotent two-sided ideal of $eRe$.
::: {.proof}
Since $R$ is left Artinian, $J(R)$ is nilpotent: $J(R)^N=0$ for some $N$. Then
$$
(eJ(R)e)^N\subseteq eJ(R)^Ne=0.
$$
Thus $eJ(R)e$ is nilpotent, and therefore
$$
eJ(R)e\subseteq J(eRe).
$$
:::

<1>6. There is an isomorphism
$$
\frac{eRe}{eJ(R)e}
\cong
\bar e\bigl(R/J(R)\bigr)\bar e,
\qquad
\bar e=e+J(R).
$$
::: {.proof}
The quotient map $R\to R/J(R)$ restricts to a surjective ring homomorphism
$$
eRe\longrightarrow \bar e(R/J(R))\bar e.
$$
Its kernel is
$$
eRe\cap J(R)=eJ(R)e,
$$
because any $x\in eRe\cap J(R)$ satisfies $x=exe$. The first isomorphism theorem gives the claim.
:::

<1>7. The quotient $(eRe)/(eJ(R)e)$ is semisimple.
::: {.proof}
The Artinian ring $R/J(R)$ is semisimple. Applying step <1>3 to the idempotent $\bar e\in R/J(R)$ shows that
$$
\bar e(R/J(R))\bar e
$$
is semisimple. Step <1>6 identifies this ring with the quotient in question.
:::

<1>8. Therefore
$$
\boxed{J(eRe)=eJ(R)e}.
$$
::: {.proof}
Put
$$
I=eJ(R)e.
$$
By step <1>5, $I\subseteq J(eRe)$. Hence
$$
J((eRe)/I)=J(eRe)/I.
$$
By step <1>7, $(eRe)/I$ is semisimple, so its Jacobson radical is zero. Therefore
$$
J(eRe)/I=0,
$$
and hence $J(eRe)=I=eJ(R)e$.
:::

<1>9. Q.E.D.
::: {.proof}
Step <1>1 answers part (a), step <1>2 and step <1>3 answer part (b), and step <1>8 proves part (c).
:::
:::
