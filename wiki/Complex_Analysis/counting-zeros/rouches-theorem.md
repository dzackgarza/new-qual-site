---
title: Rouché's theorem
order: 20
---

# Rouché's theorem

[[T-CJCKL]]

[[FT-EPR7J]] [[FT-FZERI]]

[[FT-ZJQ2T]]

:::{.slogan}
The number of zeros and poles in a region is fixed by a dominating function on the boundary.
A perturbation $m$ may be added to $M$ without changing the count, where small means $\abs{m} < \abs{M}$ on the boundary.

:::

## How to use it

:::{.remark}
The whole skill is choosing the split.

- Given $f$ and a region, find a big part $M$ and set $m \da f - M$.
  Show $\abs{m} < \abs{M}$ to conclude $\size Z_M = \size Z_f$.
  It must also be clear how many zeros $M$ has in the region, which is what makes the choice of $M$ a real choice.

- Given $f$, find a large part $M$ and show $\abs{f - M} < \abs{M}$.

- Given $\abs{m} < \abs{M}$ with no ambient $f$, you may take $f$ to be any of $\pm(M \pm m)$ and still conclude $Z_M = Z_f$.

- Given $f$ and $g$, show $\abs{f-g} < \abs{f}$ to conclude $Z_f = Z_g$.
  The symmetric form improves this to $\abs{f-g} < \abs f + \abs g$.

- A common trick: show $\abs{f-g} < 1$ together with $\abs f > 1$ or $\abs g > 1$.

- For a power series $f_n \to f$: find a *lower* bound $L$ for $f$ and an *upper* bound $U$ for the tail $f - f_n$, so that $\abs{f_n - f} < U < L < \abs f$ and $Z_f = Z_{f_n}$.

:::

:::{.proof title="of Rouché"}
Apply the argument principle to $(f+g)/f$.
Alternatively, note that $N(f+tg, \Omega)$ is a continuous $\ZZ\dash$valued function of $t \in [0,1]$, hence constant.

![](../../../../assets/assets/figures/2021-12-10_22-23-58.png)

:::

:::{.proof title="of Rouché, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-25-41.png)

![](../../../../assets/assets/figures/2021-12-15_02-24-10.png)

:::

![](../../../../assets/assets/figures/2021-10-29_01-39-19.png)

![](../../../../assets/assets/figures/2021-10-29_01-39-43.png)

## Worked counts

:::{.example title="The same polynomial, two radii, two splittings"}
Take $P(z) = z^4 + 6z + 3$.

- On $\abs{z} < 2$: set $M(z) = z^4$ and $m(z) = 6z + 3$.
  Then $\abs{m} \leq 6\abs z + 3 = 15 < 16 = \abs{M}$ on $\abs z = 2$, so $P$ has 4 zeros there.

- On $\abs{z} < 1$: the dominant term changes.
  Set $M(z) = 6z$ and $m(z) = z^4 + 3$, so $\abs{m} \leq \abs z^4 + 3 = 4 < 6 = \abs{M}$ on $\abs z = 1$, and $P$ has 1 zero there.

:::

:::{.example title="Exactly one solution"}
Claim: $\alpha z e^z = 1$ has exactly one solution in $\DD$ whenever $\abs\alpha > e$.

Set $M(z) = \alpha z$ and $m(z) = e^{-z}$.
On $\abs z = 1$, $\abs{m} = \abs{e^{-z}} = e^{-\Re(z)} \leq e < \abs\alpha = \abs{M}$.
Since $M$ has the single zero $z_0 = 0$, so does $M + m$.

:::

[[C-FRF33]]

[[C-GM57K]]

[[C-YQUHR]]

## Exercises

[[E-T4VAX]]
[[E-XQ4BS]]
[[P-FAGTL]]
[[P-YSJO3]]
[[P-WECI4]]
[[P-GW3Y7]]
[[P-ER23C]]
[[P-5S2DR]]
[[P-4JM4Y]]
[[P-4NBXB]]
