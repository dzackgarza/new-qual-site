---
title: Rouché's theorem
order: 20
topics:
- Rouché

---

# Rouché's theorem

[[T-CJCKL]]

[[FT-FZERI]]

::: {.slogan}
Adding to $M$ a function $m$ with $\abs{m} < \abs{M}$ on the boundary curve does not change the number of zeros minus poles inside it.
:::

## Forms of the hypothesis

::: {.remark}
Let $f$, $g$, $M$, $m$ be holomorphic on a neighborhood of the closed region bounded by $\gamma$, and write $Z_h$ for the number of zeros of $h$ inside $\gamma$.

- For $f = M + m$ with $\abs{m} < \abs{M}$ on $\gamma$, $Z_f = Z_M$; the theorem gives a count when $Z_M$ is known.

- If $\abs{m} < \abs{M}$ on $\gamma$, then $\abs{\pm m}<\abs M$, so each of $\pm(M \pm m)$ has $Z_M$ zeros.

- If $\abs{f-g} < \abs{f}$ on $\gamma$, then $Z_f = Z_g$.
  The symmetric form of Rouché's theorem reaches the same conclusion from $\abs{f-g} < \abs f + \abs g$ on $\gamma$.

- If $\abs{f-g} < 1$ on $\gamma$ and $\abs f \geq 1$ or $\abs g \geq 1$ on $\gamma$, then $Z_f = Z_g$.

- For partial sums $f_n$ of a power series of $f$: if $\abs f\geq L$ and $\abs{f - f_n}\leq U$ on $\gamma$ with $U < L$, then $Z_f = Z_{f_n}$.
:::

::: {.proof title="Rouché's theorem"}
On $\gamma$, $(M+m)/M = 1 + m/M$ takes values in the disc $\abs{w-1}<1$, which does not contain $0$, so the winding number of $((M+m)/M)\circ\gamma$ about $0$ is zero.
By the argument principle applied to $(M+m)/M$, whose logarithmic derivative is $(M+m)'/(M+m) - M'/M$, the zeros minus poles of $M+m$ and of $M$ agree.
Alternatively, $t\mapsto Z_{M+tm}-P_{M+tm}$ is given by a continuous integral in $t \in [0,1]$ and is integer valued, hence constant.
:::

::: {.proof title="Rouché's theorem, by homotopy"}
Let $f$ and $g$ be holomorphic near a closed curve $C$ bounding a region, with $\abs f > \abs g$ on $C$.
For $t\in[0,1]$ let $f_t \coloneqq f + tg$, so $f_0 = f$ and $f_1 = f+g$.
No $f_t$ vanishes on $C$: if $f_t(z) = 0$ with $z\in C$, then $\abs{f(z)} = t\abs{g(z)} < \abs{f(z)}$, a contradiction.
By the argument principle the number of zeros of $f_t$ inside $C$ is
$$
n_t = {1\over 2\pi i}\int_C {f_t'(z)\over f_t(z)}\dz
.$$
The integrand depends continuously on $t$ and $f_t$ never vanishes on the compact curve $C$, so $n_t$ is a continuous function of $t$.
It is integer valued, so it is constant on $[0,1]$, and $n_0 = n_1$.
:::

::: {.proof title="Rouché's theorem, by the argument of $1 + g/f$"}
If $\abs f > \abs g$ on $\gamma$, then neither $f$ nor $f+g$ vanishes on $\gamma$.
Let
$$
h(z) \coloneqq {f(z)+g(z)\over f(z)} = 1 + {g(z)\over f(z)}
.$$
The zeros of $h$ are the zeros of $f+g$ and the poles of $h$ are the zeros of $f$, counted with multiplicity.
For $z\in\gamma$, $h(z)\in B(1,1)\subseteq\theset{\Re w > 0}$, so $h\circ\gamma$ is a closed curve in the right half-plane and has winding number $0$ about $0$.
Equivalently, $\arg(f+g) = \arg f + \arg(1 + g/f)$ and the second term has zero net increase around $\gamma$.
By the argument principle, $h$ has as many zeros as poles inside $\gamma$, so $f+g$ and $f$ have the same number of zeros there.
:::

::: {.example title="Zeros of a monic polynomial in a disc"}
Let $p(z) = z^d + a_1z^{d-1} + \cdots + a_d$ with $\abs{a_i} < R^i/d$ for each $i$.
Then $p$ has $d$ zeros in $\abs z < R$.
Write $p = f + g$ with $f(z) = z^d$.
On $\abs z = R$, $\abs f = R^d$ and $\abs g \leq \sum_{i=1}^d \abs{a_i}R^{d-i} < \sum_{i=1}^d R^d/d = R^d$, so by Rouché's theorem $p$ has as many zeros in $\abs z<R$ as $z^d$, namely $d$.
:::

## Worked counts

::: {.example title="The same polynomial, two radii, two splittings"}
Let $P(z) = z^4 + 6z + 3$.

- On $\abs{z} < 2$: set $M(z) = z^4$ and $m(z) = 6z + 3$.
  Then $\abs{m} \leq 6\abs z + 3 = 15 < 16 = \abs{M}$ on $\abs z = 2$, so $P$ has 4 zeros there.

- On $\abs{z} < 1$: set $M(z) = 6z$ and $m(z) = z^4 + 3$, so $\abs{m} \leq \abs z^4 + 3 = 4 < 6 = \abs{M}$ on $\abs z = 1$, and $P$ has 1 zero there.
:::

::: {.example title="Exactly one solution"}
For $\abs\alpha > e$, the equation $\alpha z e^z = 1$ has exactly one solution in $\DD$.
It is equivalent to $\alpha z - e^{-z} = 0$.
Set $M(z) = \alpha z$ and $m(z) = -e^{-z}$.
On $\abs z = 1$, $\abs{m} = e^{-\Re(z)} \leq e < \abs\alpha = \abs{M}$.
Since $M$ has exactly one zero in $\DD$, so does $M + m$.
:::

[[C-FRF33]]

[[C-GM57K]]

[[C-YQUHR]]

## Exercises

[[E-T4VAX]] [[E-XQ4BS]] [[P-FAGTL]] [[P-YSJO3]] [[P-WECI4]] [[P-GW3Y7]] [[P-ER23C]] [[P-5S2DR]] [[P-4JM4Y]] [[P-4NBXB]]
