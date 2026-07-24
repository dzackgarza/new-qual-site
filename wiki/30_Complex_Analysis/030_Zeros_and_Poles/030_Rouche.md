# Rouché 

:::{.theorem title="Rouché's Theorem" ref="Rouche"}
Let $M, m$ be meromorphic on $\Omega$ and write $Z_M, Z_m, P_M, P_m$ for the numbers of zeros and poles of $M$ and $m$ respectively.
Suppose $\gamma \subseteq \Omega$ is a toy contour winding about each zero and pole of $f$ and $g$ precisely once.
Then
\[
\abs{m} \leq \abs{M} \text{ on } \gamma \implies \Index_{z=0}(M\circ \gamma)(z) 
&= \Index_{z=0}((M+m)\circ \gamma)(z) \\
\implies Z_M - P_M 
&= Z_{M+m} - P_{M+m}
.\]
In particular, if $M, m$ are *holomorphic* on $\Omega$, then $M$ and $M+m$ have the same number of zeros in $\Omega$, i.e. $Z_M = Z_{M+m}$.
:::

:::{.slogan}
The number of zeros/poles in a region is determined by a dominating function on the boundary.
You can add a small perturbation $m$ to $M$ and preserve the number of zeros, where "small" means $\abs{m} < \abs{M}$ on the boundary.
:::

:::{.remark}
On how to use Rouché, and some common tricks:

- Given $f$ and a region, find a big part $M$ and a small part $m \da f-M$.
  Then show $\abs{m} < \abs{M}$ to get $\size Z_M = \size Z_f$.
  - It should also be clear how many zeros $M$ has in the region!
- Given $f$, just find a large part $M$, and show $\abs{f-M} < M$.
- Given $\abs{m} < \abs{M}$ with no ambient $f$, you can freely choose $f$ to be any of $\pm (M \pm m)$ to obtain $Z_M = Z_f$
- Given $f$ and $g$, show $\abs{f-g} < \abs{f}$ to get $Z_f = Z_g$.
  - This can be improved to $\abs{f-g} < \abs{f} + \abs{g}$ using the symmetric/extended version of the theorem.
- A common trick: show $\abs{f-g} < 1$ and either $\abs{f} > 1$ or $\abs{g} > 1$.
- For power series $f_n(z) \to f(z)$: find a *lower* bound $L$ for $f$ and an *upper* bound for the tail $f - f_n$ to get $\abs{f_n - f} < U < L < \abs{f}$ to get $Z_f = Z_{f_n}$.

:::

:::{.proof title="of Rouché"}
Idea: use argument principle on $(f+g)/f$.
Alternatively, use that $N(f+tg, \Omega)$ is a continuous $\ZZ\dash$valued function for all $t\in [0, 1]$.

![](figures/2021-12-10_22-23-58.png)

:::

:::{.proof title="of Rouché, alternative"}

![](figures/2021-12-14_16-25-41.png)

![](figures/2021-12-15_02-24-10.png)

:::

# Exercises

[[P-FAGTL]]

[[P-YSJO3]]

[[P-WECI4]]

[[P-GW3Y7]]

[[P-ER23C]]

[[P-5S2DR]]

[[P-4JM4Y]]

[[P-4NBXB]]
