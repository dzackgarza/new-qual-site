---
order: 90
---

# Proofs of the fundamental theorem of algebra

::: {.theorem title="Fundamental theorem of algebra"}
Every nonconstant polynomial $P(z) = a_nz^n + \cdots + a_0\in\CC[z]$ with $a_n\neq 0$ and $n\geq 1$ has exactly $n$ zeros in $\CC$, counted with multiplicity.
:::

## By the argument principle

::: {.proof title="Using the argument principle"}
Since $\abs{P(z)}\to\infty$ as $\abs z\to\infty$, there is $R>0$ such that $P$ has no zeros in $\ts{\abs z\geq R}$.
Let $g \coloneqq P'/P$ and fix $R' > R$.
By the [[T-JXDQT|argument principle]], the number $N$ of zeros of $P$, counted with multiplicity, all of which lie in $\abs z < R'$, is
$$
N = {1\over 2\pi i} \oint_{\abs{\xi} = R'} g(\xi) \,d\xi.
$$
The function $g$ is holomorphic on $\abs z > R$ and $zg(z) = zP'(z)/P(z)\to n$ as $z\to\infty$, so on $\abs z > R$ it has a Laurent expansion $g(z) = {n\over z} + {c_2 \over z^2} + \cdots$, converging uniformly on $\abs z = R'$.
Integrating term by term gives $N = n$.
:::

## By Rouché's theorem

::: {.proof title="From Gamelin"}

![](../../../../assets/assets/figures/2021-12-10_18-02-14.png)

:::

::: {.proof title="Using Rouché's theorem"}

![](../../../../assets/assets/Complex_Analysis/figures/2021-07-29_20-41-18.png)
![](../../../../assets/assets/Complex_Analysis/figures/2021-07-29_20-41-29.png)

Let $f(z) \coloneqq a_n z^n$ and $g(z) \coloneqq P(z) - f(z) = a_{n-1}z^{n-1} + \cdots + a_0$, so $f+g = P$.
Choose
$$
R > \max\qty{ { \abs{a_{n-1}} + \cdots + \abs{a_0} \over \abs{a_n} }, 1}.
$$
For $\abs z = R$,
$$
\begin{aligned}
\abs{g(z)}
&\leq \abs{a_{n-1}}R^{n-1} + \cdots + \abs{a_1} R + \abs{a_0} && \text{triangle inequality} \\
&\leq R^{n-1} \qty{ \abs{a_{n-1}} + \cdots + \abs{a_1} + \abs{a_0} } && R>1 \\
&< R^{n-1} \cdot \abs{a_n} R && \text{choice of } R \\
&= \abs{f(z)}.
\end{aligned}
$$
By [[T-CJCKL|Rouché's theorem]], $P = f+g$ and $f$ have the same number of zeros in $\abs z<R$, namely $n$.
Every zero of $P$ lies in $\abs z < R$, since the same estimate gives $\abs{P(z)}\geq\abs{f(z)}-\abs{g(z)}>0$ for $\abs z\geq R$.
:::

## By Liouville's theorem

::: {.proof}

![](../../../../assets/assets/figures/2021-12-14_16-58-33.png)

:::

::: {.proof title="From Gamelin"}

![](../../../../assets/assets/figures/2021-12-10_19-52-51.png)

![](../../../../assets/assets/figures/2021-12-10_19-52-58.png)

:::

::: {.proof title="Using Liouville's theorem"}
It suffices to show that $P$ has a zero; the full count follows by induction on $n$ after dividing by $z - z_0$ for a zero $z_0$.
Suppose $P$ has no zeros, so that $1/P$ is entire.

Write $P(z) = z^n \qty{a_n + \frac{a_{n-1}}{z}+\cdots+\frac{a_{0}}{z^{n}}}$.
The bracket tends to $a_n$ as $z\to\infty$, so there is $R>0$ with $\abs{P(z)} \geq B$ for $\abs z\geq R$, where $B \coloneqq \abs{a_n}R^n/2 > 0$.
On the compact disc $\abs z\leq R$ the continuous function $\abs P$ attains a minimum $A$, and $A>0$ because $P$ has no zeros.
With $C \coloneqq \min(A, B)$, $\abs{P(z)}\geq C$ on $\CC$, so $\abs{1/P(z)}\leq 1/C$ on $\CC$.
By [[T-QHIHJ|Liouville's theorem]] $1/P$ is constant, so $P$ is constant, a contradiction.
:::

## By the open mapping theorem

::: {.proof title="Using the open mapping theorem"}
Extend $P$ to a holomorphic map $P\colon \PP^1(\CC) \to \PP^1(\CC)$ with $P(\infty) = \infty$.
Its image is compact, since $\PP^1(\CC)$ is compact, and hence closed, since $\PP^1(\CC)$ is Hausdorff.
Since $P$ is nonconstant, the image is open by the [[C-FRF33|open mapping theorem]] applied in local coordinates.
The image is nonempty and $\PP^1(\CC)$ is connected, so the image is all of $\PP^1(\CC)$.
In particular $0 = P(z_0)$ for some $z_0$, and $z_0\neq\infty$ because $P(\infty)=\infty$.
:::

## By the generalized Liouville theorem

[[T-BBQLQ]]

[[L-ZXBBI]]

::: {.proof title="Using the lemma on maps from compact Riemann surfaces"}
Extend $P$ to a nonconstant holomorphic map $P\colon \PP^1(\CC) \to \PP^1(\CC)$ with $P(\infty) = \infty$.
Since $\PP^1(\CC)$ is compact, $P$ is surjective by [[L-ZXBBI]], so $P(z_0) = 0$ for some $z_0\in\PP^1(\CC)$, and $z_0\neq\infty$.
:::

## Singularities and omitted values

The following results are developed on [[complex-analysis/singularities/index|Singularities]].

[[T-ISZP3]]

[[T-HWBWI]]

## Zero divisors

::: {.proposition}
The ring of holomorphic functions on a domain in $\CC$ has no zero divisors.
:::

::: {.proof}
Let $fg \equiv 0$ with $f\not\equiv 0$.
By the [[T-SVF2W|identity principle]] the zero set of $f$ is discrete, so $g$ vanishes on its complement, which has a limit point in the domain.
So $g\equiv 0$ by the identity principle again.
:::

## A Banach space of holomorphic functions

The following exercise is solved using Morera's theorem.

[[E-QO2S7]]
