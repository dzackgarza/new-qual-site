# Montel


:::{.remark}
"Locally" means "on all compact subsets".
:::


## Equicontinuity

:::{.definition title="Equicontinuous Family"}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that 
\[
\abs{x-y}<\eps \implies \abs{f_n(x) - f_n(y)} < \eps
&& \forall n
.\]
:::

:::{.slogan}
Equicontinuity is uniform continuity which is also uniform across the family.
:::

:::{.theorem title="Arzelà-Ascoli (analog of Heine-Borel)"}
For $X$ compact Hausdorff, consider the Banach space $C(X; \RR)$ equipped with the *uniform norm* 
\[
\norm{f}_{\infty, X} \da \sup_{x\in X} \abs{f(x)}
.\]

A subset $A \subseteq C(X; \RR)$ is compact iff $A$ is closed, uniformly bounded, and equicontinuous.

For $X = [a,b]\subseteq \RR$, if a sequence is uniformly bounded and uniformly equicontinuous, then there exists a uniformly convergent subsequence.
:::

:::{.remark}
If $A$ is a sequence of continuous functions, it contains a subsequence converging uniformly and the limit is continuous.
The proof is an $\eps/3$ argument.
:::

## Normal Families

:::{.definition title="Normal Family"}
A family of functions $\mcf \da \ts{f_j}_{j\in J}$ is **normal** iff every sequence $\ts{f_k}$ has a subsequence that converges locally uniformly, i.e. $\ts{f_{k_i}}$ converges uniformly on every compact subset.

:::

:::{.theorem title="Locally equicontinuous iff normal when uniformly bounded"}
Suppose $\mcf$ is locally uniformly bounded. 
Then $\mcf$ is locally equicontinuous and a normal family.
:::

:::{.definition title="Univalent functions"}
A function $f\in \Hol(U; \CC)$ is called **univalent** if $f$ is injective.
:::

:::{.remark}
If $f: \Omega \to \Omega'$ is a univalent surjection, $f$ is invertible on $\Omega$ and $f\inv$ is holomorphic.
Compare to real functions: $f(x) = x^3$ is injective on $(-c, c)$ for any $c$ but $f'(0) = 0$ and $f\inv(x) \da x^{1/3}$ is not differentiable at zero.
:::

:::{.definition title="Normal Families"}
A family $\mcf = \ts{f_j}_{j\in J}$ of holomorphic functions on $\Omega$ is **normal** if every sequence of functions from $\mcf$ has a locally uniformly convergent subsequence (so they converge on every compact subset of $\Omega$).
:::

:::{.definition title="Uniform boundedness and equicontinuity"}
A family $\mcf$ of holomorphic functions is **uniformly bounded on compact subsets of $\Omega$** iff for each compact $K \subseteq \Omega$ if
\[
\exists M>0 \text{ such that } \abs{f(z)} < M \qquad \forall z\in K,\,\forall f\in \mcf
.\]
:::

:::{.definition title="Equicontinuity"}
A family $\mcf$ of holomorphic functions is **equicontinuous** on $K$ if 
\[
\forall \eps>0,\, \exists \delta = \delta(\eps) \text{ such that } z,w\in K,\, \abs{z-w}< \delta \implies \abs{f(z) - f(w)} < \eps \quad \forall f\in \mcf
.\]
:::

:::{.remark}
Equicontinuity is uniform continuity, where the uniformity extends across all $f\in \mcf$.
The following is a stark difference between holomorphic and smooth functions, and is used in the Riemann mapping theorem:
:::

:::{.example title="Negating equicontinuity"}
To negate equicontinuity, show that there exists $\eps>0$ and a bad tuple $(x, y, f\in \mcf)$ such that for any $\delta$, we can arrange $\abs{x-y} < \delta$ to be small but $\abs{f(x) - f(y)} > \eps$ is large.
This produces sequences $x_k, y_k, f_k$ with $\abs{x_k-y_k}\to 0$ but $\abs{f_k(x_k) - f_k(y_k)} > \eps$.
:::

[[E-ISFYB]]
[[E-LXY7N]]
[[E-YFL4K]]
## Montel's Theorem

:::{.theorem title="Montel's theorem"}
If $\mcf$ is a family of locally uniformly bounded holomorphic functions on $\Omega$, then

- $\mcf$ is a normal family by Arzela-Ascoli, and
- $f$ is locally equicontinuous (so equicontinuous on every compact subset).

Equivalently: a family $\mcf$ of meromorphic functions on a domain $\Omega$ that omits three values is normal.
:::

:::{.slogan}
Locally uniformly bounded families are normal.
For bounded sequences of holomorphic functions, pointwise convergence is the same as uniform convergence on bounded sets.
:::

:::{.remark}
This says that a sequence of holomorphic functions avoiding the exterior of a disc contains a locally uniformly convergent subsequence.
In particular, the limit is holomorphic.

Moreover, if $f_n\to f$ pointwise where $f$ fails continuity or differentiability at a single point, then $\ts{f_n}$ can not be uniformly bounded on all compact subsets.
:::

## Exercise

[[E-UJAF4]]
[[E-C5QHZ]]
[[E-GFNDF]]
