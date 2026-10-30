---
schema: qual/card@1
id: P-MAXAT-4-03
kind: problem
title: Homology and cohomology ring of the loop space $\Omega S^n$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 4, problem 3 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Calculate $H _ { * } ( \Omega S ^ { n } )$ and the ring structure on $H ^ { \ast } ( \Omega S ^ { n } )$
:::

::: {.solution}

Assume $n\geq2$ and use integral coefficients. Put $d=n-1$.

::: pf

::: {.pf-step #s1-1}

The James--Bott--Samelson theorem gives
$$
H_*(\Omega S^n;\ZZ)
\cong T(t_d),
\qquad \gradeddegree{t_d}=d,
$$
as a graded algebra under the Pontryagin product.


::: pf-proof

Since $S^n=\Sigma S^{n-1}$, the James construction $J(S^{n-1})$ is homotopy equivalent to $\Omega\Sigma S^{n-1}=\Omega S^n$. The James filtration has associated graded homology the tensor algebra on the reduced homology of $S^{n-1}$. Because
$$
\widetilde H_*(S^{n-1};\ZZ)=\ZZ\{t_d\}
$$
is free on one class of degree $d$, Bott--Samelson identifies the Pontryagin algebra with $T(t_d)$.

:::

:::

::: {.pf-step #s1-2}

Since there is only one generator, additively
$$
H_q(\Omega S^n;\ZZ)
\cong
\begin{cases}
\ZZ,&q=jd\text{ for some }j\geq0,\\
0,&\text{otherwise}.
\end{cases}
$$


::: pf-proof

The tensor algebra on one generator has basis
$$
1,t,t^2,t^3,\ldots,
$$
with $\gradeddegree{t^j}=jd$. Thus it has rank one exactly in the displayed degrees.

:::

:::

::: {.pf-step #s1-3}

The cohomology ring is the graded Hopf dual of the homology Hopf algebra. If $x_j\in H^{jd}(\Omega S^n;\ZZ)$ is dual to $t^j$, then
$$
x_i x_j
=\sum_{\sigma\in\operatorname{Sh}(i,j)}
\epsilon(\sigma),x_{i+j},
$$
where $\epsilon(\sigma)$ is the Koszul sign obtained by shuffling degree-$d$ generators.


::: pf-proof

Cup product in cohomology is dual to the coproduct in homology. Under the James model, the diagonal induces the shuffle coproduct on tensor words. Pairing the coproduct of $t^{i+j}$ with $x_i\otimes x_j$ sums the Koszul signs of all $(i,j)$-shuffles, giving the stated coefficient.

:::

:::

::: {.pf-step #s1-4}

If $n$ is odd, then $d$ is even and all shuffle signs are $+1$. Hence
$$
x_i x_j=\binom{i+j}{i}x_{i+j}.
$$


::: pf-proof

When $d$ is even, interchanging two degree-$d$ factors contributes sign $(-1)^{d^2}=1$. There are exactly $\binom{i+j}{i}$ $(i,j)$-shuffles, so step [](#s1-3){.pf-ref} reduces to the displayed formula.

:::

:::

::: {.pf-step #s1-5}

Thus, for $n=2m+1$,
$$
\boxed{
H^*(\Omega S^{2m+1};\ZZ)
\cong\Gamma_{mathbb Z}(x_{2m}),}
$$
the divided-power algebra on a class of degree $2m$.


::: pf-proof

The defining multiplication in the divided-power algebra is
$$
\gamma_i(x)\gamma_j(x)
=\binom{i+j}{i}\gamma_{i+j}(x).
$$
Identify $x_j$ from step [](#s1-4){.pf-ref} with $\gamma_j(x_{2m})$.

:::

:::

::: {.pf-step #s1-6}

If $n$ is even, then $d$ is odd. The signed shuffle sum is zero when both $i$ and $j$ are odd and otherwise equals the corresponding unsigned binomial coefficient after pairing adjacent odd letters. Equivalently,
$$
H^*(\Omega S^{2m};\ZZ)
\cong
\Lambda(a_{2m-1})\otimes
\Gamma_{mathbb Z}(b_{4m-2}),
$$
where $b$ corresponds to the dual of $t^2$.


::: pf-proof

For odd $d$, the basic degree-$d$ class $a=x_1$ satisfies $a^2=0$ by graded commutativity and torsion-freeness. The even tensor powers $t^{2j}$ define classes $\gamma_j(b)=x_{2j}$ of degree $2jd$, and their shuffle coefficients are the ordinary divided-power coefficients after grouping the odd generators in pairs. The odd-index classes are $a\gamma_j(b)=x_{2j+1}$. Thus the graded group from step [](#s1-2){.pf-ref} and the signed shuffle multiplication of step [](#s1-3){.pf-ref} are exactly the tensor product $\Lambda(a)\otimes\Gamma(b)$, with $\gradeddegree{a}=d=2m-1$ and $\gradeddegree{b}=2d=4m-2$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{H_*(\Omega S^n;\ZZ)=T(t_{n-1})}
$$
and
$$
\boxed{
H^*(\Omega S^n;\ZZ)
\cong
\begin{cases}
\Gamma(x_{n-1}),&n\text{ odd},\\
\Lambda(a_{n-1})\otimes\Gamma(b_{2n-2}),&n\text{ even}.
\end{cases}}
$$


::: pf-proof

The homology statement is step [](#s1-1){.pf-ref}. The two cohomology cases are steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives both the requested homology and the full integral cohomology-ring structure.

:::

:::

:::
