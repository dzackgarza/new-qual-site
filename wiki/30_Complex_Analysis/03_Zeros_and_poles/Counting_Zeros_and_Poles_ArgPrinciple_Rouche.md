---
order: 16
---

# Counting Zeros and Poles

## Argument Principle

[[D-IA5FS]]

[[E-VI5ZS]]

:::{.remark}
Note that the logarithmic derivative picks up the valuation:
\[
d \qty{ \log(f) } = {f'\over f}\dz  \implies \Res_{z=p}(d \log(f) ) = v_p(f)
.\]

:::

[[D-QEVVE]]

[[T-VCX3Y]]

:::{.proof}
\envlist

- If $z_0$ is a zero of $f$ of order $m$, write $f(z) = (z-z_0)^m g(z)$ with $g(z)$ holomorphic and nonzero on some neighborhood of $z_0$.
- Compute
\[
\del_{\log} f(z)
&=
\frac{m\left(z-z_{0}\right)^{m-1} g(z)+\left(z-z_{0}\right)^{m} g^{\prime}(z)}{\left(z-z_{0}\right)^{m} g(z)} \\
&= {m \over z-z_0} + \del_{\log} g(z)
,\]
so $z_0$ is a simple pole of $\del_{\log} f$ and $\res_{z=z_0} \del_{\log} f = m$.

- If $z_0$ is a pole of $f$ of order $m$, write $f(z) = (z-z_0)^{-m} g(z)$, then
\[
\del_{\log} f = {-m \over z-z_0} + \del_{\log} g
,\]
  so $z_0$ is a simple pole and $\Res_{z=z_0} \del_{\log f} = -m$.

- Now apply the residue theorem, and group residues according to sign:
\[
{1\over 2\pi i } \int_{\gamma} \del_{\log }f(z) \dz
&= \sum_{z_i \in P_{\del_{\log} f}} \Res_{z=z_i} \del_{\log} f(z)\\
&= \sum_{z_k \in Z_f} \Res_{z=z_k} f(z) - \sum_{z_j \in P_f} \Res_{z=z_j} f(z)
.\]

:::

[[T-EBAOE]]

:::{.proof}
Make the change of variables $w = f(z)$, then $z=\gamma(t) \mapsto w = (f\circ \gamma)(t)$ and $\dw = f'(z) \dz$, so
\[
{1\over 2\pi i }\int_{\gamma} \del_{\log} f(z) \dz
= {1\over 2\pi i} \int_{f\circ \gamma} {1\over w} \dw \da \Ind_{w=0} (f\circ \gamma)(w)
.\]

:::

:::{.example title="Using the index version of the argument principle"}
Let $f(z) = z^2 + z = z(z+1)$.

- $\gamma_1 \da \ts{\abs z = 2}$ contains 2 zeros and 0 poles, so $f\circ \gamma$ winds twice around zero counterclockwise.
- $\gamma_2 \da \ts{\abs z = {1\over 2}}$ contains 1 zero and 0 poles, so $f\circ \gamma$ winds once.

:::

## Rouché

[[T-5JNUU]]

:::{.slogan}
The number of zeros/poles are determined by a dominating function.

:::

![](../../../../assets/assets/figures/2021-10-29_01-39-19.png)

![](../../../../assets/assets/figures/2021-10-29_01-39-43.png)

[[E-T4VAX]]
[[E-XQ4BS]]
[[C-FRF33]]

[[C-GM57K]]

[[C-YQUHR]]

## Counting Zeros

:::{.example}
\envlist

- Take $P(z) = z^4 + 6z + 3$.
- On $\abs{z} < 2$:
  - Set $f(z) = z^4$ and $g(z) = 6z + 3$, then $\abs{g(z)} \leq 6\abs{z} + 3 = 15 < 16= \abs{f(z)}$.
  - So $P$ has 4 zeros here.
- On $\abs{z} < 1$:
  - Set $f(z) = 6z$ and $g(z) = z^4 + 3$.
  - Check $\abs{g(z)} \leq \abs{z}^4 + 3 = 4 < 6 = \abs{f(z)}$.
  - So $P$ has 1 zero here.

:::

:::{.example}
\envlist

- Claim: the equation $\alpha z e^z = 1$ where $\abs{\alpha} > e$ has exactly one solution in $\DD$.
- Set $f(z) = \alpha z$ and $g(z) = e^{-z}$.
- Estimate at $\abs{z} =1$ we have $\abs{g} =\abs{e^{-z}} = e^{-\Re(z)} \leq e^1 < \abs{\alpha} = \abs{f(z)}$
- $f$ has one zero at $z_0 = 0$, thus so does $f+g$.

:::
