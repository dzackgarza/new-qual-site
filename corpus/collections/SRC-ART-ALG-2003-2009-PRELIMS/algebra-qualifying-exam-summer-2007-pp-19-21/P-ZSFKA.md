---
schema: qual/card@1
id: P-ZSFKA
kind: problem
title: The ring of integers of $\mathbb{Q}(\sqrt{2})$ is a Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Number Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared Summer 2007 Rings 3 with the retained extraction; made the absolute-value convention explicit and corrected the subject classification."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the integral-coordinate argument, multiplicativity and positivity of the absolute norm, and the uniform three-quarter remainder bound."
---

::: {.problem}
Let $O$ be the ring of integers of $\mathbf{Q}(\sqrt2)$.
Show that $O$ is a Euclidean domain with respect to the absolute field norm
$$
\delta(a+b\sqrt2)=\left|a^2-2b^2\right|.
$$
:::

::: solution
<1>1. The ring of integers is $O=\mathbb Z[\sqrt2]$.

::: proof
For $a,b\in\mathbb Z$, the element $a+b\sqrt2$ satisfies the monic
polynomial
$$
T^2-2aT+(a^2-2b^2)\in\mathbb Z[T],
$$
so it is an algebraic integer.

Conversely, write an algebraic integer in $\mathbb Q(\sqrt2)$ as
$\alpha=a+b\sqrt2$, with $a,b\in\mathbb Q$. If $b=0$, the rational
root theorem applied to a monic integer polynomial for $\alpha$
gives $a\in\mathbb Z$.

Suppose $b\ne0$. Then $\alpha$ has degree $2$, with minimal polynomial
$T^2-2aT+(a^2-2b^2)$. A monic factor over $\mathbb Q$ of a monic
integer polynomial has integer coefficients, by Gauss's lemma
[@DF04]. Therefore
$$
2a=m\in\mathbb Z,\qquad a^2-2b^2=n\in\mathbb Z,
\qquad 8b^2=m^2-4n\in\mathbb Z.
$$
Write $b=u/v$ in lowest terms with $v>0$. The last integrality
condition gives $v^2\mid8u^2$, hence $v^2\mid8$ and $v\in\{1,2\}$.
Thus $b=k/2$ for an integer $k$, and
$$
m^2-2k^2=4n.
$$
If $k$ were odd, this would give $m^2\equiv2\pmod4$, impossible
because squares modulo $4$ are $0$ and $1$. Hence $k$ is even;
then the same equality makes $m$ even. Consequently $a=m/2$ and
$b=k/2$ are both integers. This proves the asserted equality of rings.
:::

<1>2. The absolute norm is multiplicative and is a positive integer
on every nonzero element of $O$.

::: proof
Conjugation $\tau(a+b\sqrt2)=a-b\sqrt2$ is an automorphism of the
field. Thus
$$
N(\alpha)=\alpha\tau(\alpha),\qquad
N(\alpha\beta)=N(\alpha)N(\beta),
$$
and absolute values give multiplicativity of $\delta=|N|$.
Step <1>1 makes $N$ integer-valued on $O$. If $\alpha\ne0$, then
both $\alpha$ and $\tau(\alpha)$ are nonzero field elements, so
$\delta(\alpha)$ is a positive integer.
:::

<1>3. Euclidean division holds for $\delta$.

::: proof
Let $\alpha,\beta\in O$ with $\beta\ne0$, and write
$$
\frac{\alpha}{\beta}=u+v\sqrt2,\qquad u,v\in\mathbb Q.
$$
Choose integers $m,n$ such that $|u-m|\leq1/2$ and $|v-n|\leq1/2$,
and put $q=m+n\sqrt2\in O$ and $r=\alpha-\beta q\in O$.
If $r=0$, the division has zero remainder. Otherwise step <1>2 gives
$$
\begin{aligned}
\delta(r)
&=\delta(\beta)\left|(u-m)^2-2(v-n)^2\right|\\
&\leq\delta(\beta)\bigl((u-m)^2+2(v-n)^2\bigr)\\
&\leq\frac34\delta(\beta)<\delta(\beta).
\end{aligned}
$$
Thus $\alpha=\beta q+r$ with zero remainder or strictly smaller
positive integer size. Since $O$ is a subring of a field, it is an
integral domain, and this proves that it is Euclidean. Under the
definition also requiring $\delta(\alpha)\leq\delta(\alpha\beta)$
for nonzero $\alpha,\beta$, that condition follows from
multiplicativity and $\delta(\beta)\geq1$.
:::
:::

::: remark
The signed field norm is $N(a+b\sqrt2)=a^2-2b^2$; the Euclidean
function is its absolute value. The signed values
$N(n\sqrt2)=-2n^2$ are unbounded below and cannot serve as the
nonnegative integer size in the Euclidean algorithm.
:::
