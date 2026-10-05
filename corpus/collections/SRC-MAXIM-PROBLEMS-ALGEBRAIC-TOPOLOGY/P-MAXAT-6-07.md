---
schema: qual/card@1
id: P-MAXAT-6-07
kind: problem
title: Maxim algebraic topology 6.7
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 7 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that $\mathbb { C P } ^ { 4 }$ cannot be smoothly embedded in $\mathbb { R } ^ { n }$ with $n \leq 1 1$ . (Hint: use Pontrjagin classes)
:::

::: {.solution}
The real dimension of $\mathbb{CP}^4$ is $8$. Suppose, for contradiction, that there is a smooth embedding
\[
\mathbb{CP}^4\hookrightarrow\mathbb R^N
\qquad(N\leq11),
\]
and let $\nu$ be its normal bundle.

<1>1. The normal bundle has rank
\[
r=N-8\leq3
\]
and satisfies
\[
T\mathbb{CP}^4\oplus\nu\cong\varepsilon^N.
\]

::: {.proof}
For a smooth embedding, the restricted tangent bundle of Euclidean space splits as the tangent bundle of the submanifold plus its orthogonal normal bundle. Since $\dim_{\mathbb R}\mathbb{CP}^4=8$, the normal rank is $N-8$.
:::

<1>2. Let
\[
x\in H^2(\mathbb{CP}^4;\mathbb Z)
\]
be the positive generator. Then
\[
p(T\mathbb{CP}^4)=(1+x^2)^5.
\]

::: {.proof}
The complex Euler sequence gives the stable complex-bundle identity
\[
T\mathbb{CP}^4\oplus\varepsilon^1_{\mathbb C}
\cong5\gamma^*,
\]
where $c_1(\gamma^*)=x$. The underlying real bundle of a complex line with first Chern class $x$ has total Pontryagin class $1+x^2$. Pontryagin classes are stable and multiplicative, giving the formula.
:::

<1>3. Since
\[
H^*(\mathbb{CP}^4;\mathbb Z)
=\mathbb Z[x]/(x^5),
\]
the tangent Pontryagin class is
\[
p(T\mathbb{CP}^4)
=1+5x^2+10x^4.
\]

::: {.proof}
Expand
\[
(1+x^2)^5
=1+5x^2+10x^4+10x^6+5x^8+x^{10}.
\]
Since $x^5=0$, all terms involving $x^6$ or higher vanish.
:::

<1>4. From the stable trivialization in step <1>1,
\[
p(\nu)=p(T\mathbb{CP}^4)^{-1}.
\]

::: {.proof}
Whitney multiplicativity gives
\[
p(T\mathbb{CP}^4)p(\nu)=p(\varepsilon^N)=1.
\]
Thus the normal total Pontryagin class is the multiplicative inverse.
:::

<1>5. Through degree $8$,
\[
p(\nu)=1-5x^2+15x^4.
\]

::: {.proof}
Write
\[
(1+5x^2+10x^4)^{-1}=1+Ax^2+Bx^4.
\]
Multiplication gives
\[
1+(A+5)x^2+(B+5A+10)x^4.
\]
Setting the positive-degree coefficients equal to zero yields
\[
A=-5,
\qquad
B=25-10=15.
\]
:::

<1>6. The decisive obstruction is $p_2(\nu)$: because $\operatorname{rank}\nu\leq3$,
\[
p_2(\nu)=0,
\]
but step <1>5 gives
\[
p_2(\nu)=15x^4\ne0.
\]

::: {.proof}
For a real rank-$r$ bundle, $p_i$ vanishes for $2i>r$ because after applying the splitting principle there are only $\lfloor r/2\rfloor$ Pontryagin roots; equivalently $p_i=(-1)^ic_{2i}(E\otimes\mathbb C)$ and the special real structure forces $p_i=0$ for $i>\lfloor r/2\rfloor$. In particular a rank-$3$ bundle has no $p_2$. On the other hand, step <1>5 identifies $p_2(\nu)$ with $15x^4$, and
\[
x^4\ne0\in H^8(\mathbb{CP}^4;\mathbb Z).
\]
This is the required contradiction.
:::

<1>7. Therefore
\[
\boxed{
\mathbb{CP}^4\text{ cannot be smoothly embedded in }
\mathbb R^N\text{ for }N\leq11.}
\]

::: {.proof}
Any such embedding would produce the rank-$\leq3$ normal bundle of step <1>1, contradicting step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the desired nonembedding statement.
:::
:::
