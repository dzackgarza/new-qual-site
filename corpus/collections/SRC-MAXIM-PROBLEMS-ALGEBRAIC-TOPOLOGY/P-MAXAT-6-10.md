---
schema: qual/card@1
id: P-MAXAT-6-10
kind: problem
title: Maxim algebraic topology 6.10
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 10 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find obstructions to the existence of a complex structure on an even dimensional manifold.
:::

::: {.solution}
Let $M^{2n}$ be a smooth manifold. A complex structure on $TM$ means a bundle endomorphism
\[
J:TM\to TM,
\qquad J^2=-1,
\]
equivalently a reduction of the structure group from $GL_{2n}(\mathbb R)$ to $GL_n(\mathbb C)$. This imposes several characteristic-class obstructions.

<1>1. A complex vector bundle has a canonical orientation. Hence a necessary condition is
\[
\boxed{w_1(TM)=0.}
\]

::: {.proof}
The real determinant of a complex-linear automorphism is positive: if $A\in GL_n(\mathbb C)$, then
\[
\det_{\mathbb R}A=|\det_{\mathbb C}A|^2>0.
\]
Thus a reduction to $GL_n(\mathbb C)$ reduces the real structure group to $GL^+_{2n}(\mathbb R)$, which is equivalent to orientability and hence to $w_1(TM)=0$.
:::

<1>2. If $TM$ is the underlying real bundle of a complex bundle $E$, then
\[
w_{2i+1}(TM)=0,
\qquad
w_{2i}(TM)=\rho_2(c_i(E)),
\]
where $\rho_2$ denotes reduction modulo $2$.

::: {.proof}
For every complex vector bundle $E$, the Stiefel--Whitney classes of its underlying real bundle satisfy
\[
w(E_{\mathbb R})=\rho_2(c(E)).
\]
Since $c_i(E)$ lies in degree $2i$, there are no odd-degree components, giving the two displayed identities.
:::

<1>3. In particular,
\[
\boxed{w_2(TM)\text{ must admit an integral lift}.}
\]
Equivalently,
\[
\boxed{\beta(w_2(TM))=W_3(TM)=0.}
\]

::: {.proof}
Step <1>2 gives
\[
w_2(TM)=\rho_2(c_1(E)).
\]
Thus $c_1(E)\in H^2(M;\mathbb Z)$ is an integral lift. In the coefficient exact sequence
\[
0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0,
\]
a mod-$2$ class lifts integrally exactly when its Bockstein vanishes. The Bockstein of $w_2$ is the integral Stiefel--Whitney class $W_3$.
:::

<1>4. The Pontryagin classes must be expressible in terms of integral Chern classes by
\[
\boxed{
p_i(TM)=(-1)^ic_{2i}(E\oplus\overline E).}
\]
Equivalently, under the splitting principle with Chern roots $x_1,\ldots,x_n$,
\[
\boxed{p(TM)=\prod_{j=1}^n(1+x_j^2).}
\]

::: {.proof}
For a complex bundle $E$,
\[
E_{\mathbb R}\otimes\mathbb C\cong E\oplus\overline E.
\]
By definition,
\[
p_i(E_{\mathbb R})=(-1)^ic_{2i}(E_{\mathbb R}\otimes\mathbb C).
\]
If $x_j$ are the Chern roots of $E$, those of $\overline E$ are $-x_j$, yielding the product formula.
:::

<1>5. The Euler class must agree with the top Chern class for the complex orientation:
\[
\boxed{e(TM)=c_n(E).}
\]
Consequently, for closed $M$,
\[
\boxed{\chi(M)=\langle c_n(E),[M]\rangle.}
\]

::: {.proof}
For a complex rank-$n$ bundle, the Euler class of the underlying oriented real rank-$2n$ bundle equals its top Chern class. For a closed oriented manifold, Poincare--Hopf gives
\[
\langle e(TM),[M]\rangle=\chi(M).
\]
Combining the two identities gives the characteristic-number condition.
:::

<1>6. Thus any proposed complex structure requires integral classes
\[
c_i\in H^{2i}(M;\mathbb Z),
\qquad1\leq i\leq n,
\]
satisfying simultaneously
\[
\rho_2(c_i)=w_{2i}(TM),
\]
the Pontryagin identities of step <1>4, and
\[
c_n=e(TM).
\]

::: {.proof}
These are exactly the necessary identities from steps <1>2, <1>4, and <1>5 applied to the hypothetical complex tangent bundle $E=(TM,J)$.
:::

<1>7. Failure of any one of these identities obstructs a complex structure on $M$.

::: {.proof}
If a complex structure existed, all identities in steps <1>1--<1>6 would necessarily hold. Their contrapositives therefore give obstructions. These conditions are not asserted to be sufficient in arbitrary dimension; higher obstruction classes may remain in the reduction problem
\[
SO(2n)/U(n)\to BU(n)\to BSO(2n).
\]
:::

<1>8. In summary, characteristic-class obstructions include
\[
\boxed{w_1=0,\quad w_{2i+1}=0,\quad W_3=\beta w_2=0,}
\]
together with compatibility of $w_{2i}$, $p_i$, and $e$ with integral Chern classes as in steps <1>2, <1>4, and <1>5.

::: {.proof}
This simply collects the necessary conditions already proved.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>8 provide the requested obstructions to reducing the tangent bundle to a complex vector bundle.
:::
:::
