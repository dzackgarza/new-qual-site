---
title: Rouché's theorem
order: 20
topics:
- Rouché

---

# Rouché's theorem

[[T-CJCKL]]

[[FT-EPR7J]] [[FT-FZERI]]

[[FT-ZJQ2T]]

::: {.slogan}
Adding to $M$ a function $m$ with $\abs{m} < \abs{M}$ on the boundary curve does not change the number of zeros minus poles inside it.
:::

## Forms of the hypothesis

::: {.remark}
The following are the same theorem for holomorphic functions on a neighborhood of the closed region bounded by $\gamma$.

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

![](../../../../assets/assets/figures/2021-12-10_22-23-58.png)
:::

::: {.proof title="Rouché's theorem, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-25-41.png)

![](../../../../assets/assets/figures/2021-12-15_02-24-10.png)
:::

![](../../../../assets/assets/figures/2021-10-29_01-39-19.png)

![](../../../../assets/assets/figures/2021-10-29_01-39-43.png)

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
