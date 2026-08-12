# Zeros and Singularities


:::{.remark}
On notation: for an analytic function $f$ expanded as a power series about $a$, write $v_a(f)$ as the $a\dash$adic valuation of $f$: expanding $f(z) = \sum_{k\in \ZZ} a_k (z-a)^k$ about $a$, define $v_a(f) = n$ iff $a_n\neq 0$ but $a_{\leq n} = 0$.
:::


[[D-VAXQT]]

[[D-BQLJV]]

:::{.remark}
Singularities can be classified by Laurent expansions $f(z) = \sum_{k\in \ZZ} c_k z^k$:

- Essential singularity: infinitely many negative terms.
- Pole of order $N$: truncated at $k = -N$, so $c_{N-\ell} = 0$ for all $\ell$.
- Removable singularity: truncated at $k=0$, so $c_{\leq -1} = 0$.
:::

:::{.example title="Removable singularities"}
\envlist

- $f(z) \da \sin(z)/z$ has a removable singularity at $z=0$, and one can redefine $f(0) \da 1$.
- If $f(z) = p(z)/q(z)$ with $q(z_0)=0$ and $p(z_0)=0$, then $z_0$ is removable with $f(z_0)\da p'(z_0)/q'(z_0)$.
:::

:::{.example title="Essential singularities"}
$f(z) \da e^{1/z}$ has an essential singularity at $z=0$, since we can expand and pick up infinitely many negative terms:
\[
e^{1/z} = 1 + {1\over z} + {1\over 2! z^2} + \cdots
.\]
In fact there exists a neighborhood of zero such that $f(U) = \CC\smz$.
Similarly $g(z) \da \sin\qty{1\over z}$ has an essential singularity at $z=0$, and there is a neighborhood $V$ of zero such that $g(V) = \CC$.
:::

:::{.example title="?"}
The singularities of a rational function are always isolated, since there are finitely many zeros of any polynomial.
The function $F(z) \da \Log(z)$ has a singularity at $z=0$ that is **not** isolated, since every neighborhood intersects the branch cut $(-\infty, 0) \cross \ts{ 0 }$, where $F$ is not even defined.
The function $G(z) \da 1/\sin(\pi/z)$ has a non-isolated singularity at 0 and isolated singularities at $1/n$ for all $n$.
:::

:::{.warnings}
$f(z) \da z^{1\over 2}$ has a singularity at zero that does not fall under this classification -- $z=0$ is a **branch singularity** and admits no Laurent expansion around $z=0$.

A similar example: $\qty{z(z-1)}^{1\over 2}$ has two branch singularities at $z=0, 1$.
:::



[[T-LZ6KG]]

:::{.proof title="?"}
Take $\gamma$ to be a circle centered at $z_0$ and use
\[
f(z) \da \int_\gamma { f(\xi) \over \xi - z} \dx
.\]
This is valid for $z\neq z_0$, but the right-hand side is analytic. (?)
:::

![](../../../../assets/assets/figures/2021-10-29_01-30-50.png)

![](../../../../assets/assets/figures/2021-10-29_01-31-06.png)


[[T-TNR7B]]


[[D-65VIK]]



[[D-R4BDD]]

[[D-OUJVC]]


[[D-VKP6N]]

[[T-EO65T]]

:::{.slogan}
The image of a punctured disc at an essential singularity is dense in $\CC$.
:::

:::{.proof title="of Casorati-Weierstrass"}
Pick $w\in \CC$ and suppose toward a contradiction that $D_R(w) \intersect f(V)$ is empty.
Consider
\[
g(z) \da {1\over f(z) - w}
,\]
and use that it's bounded to conclude that $z_0$ is either removable or a pole for $f$.
:::


[[D-BPBSQ]]

[[D-7DFVJ]]


[[T-UBWL2]]


:::{.proof title="?"}
Consider $f(z) - P(z)$, subtracting off the principal part at each pole $z_0$, to get a bounded entire function and apply Liouville.
:::






[[T-KOZO4]]

## Exercises

[[P-DO7TE]]
