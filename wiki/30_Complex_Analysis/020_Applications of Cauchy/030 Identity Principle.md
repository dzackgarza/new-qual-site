# The Identity/Continuation Principle

[[D-TFSPT]]

[[T-SVF2W]]

:::{.slogan}
Two functions agreeing on a set with a limit point are equal on a domain.

:::

:::{.proof title="Using power series and topology"}
$1\implies 2$:
Take $z_k \da z_0 + C{1\over k}$ for any $z_0\in \Omega$, since $f(z_0) = 0$ for any such $z_k$.
Choose the constant $C$ such that $z_k \in \Omega$ for all $k$.

$2\implies 3$:
Given such a $z_0$, take a Laurent expansion centered there.
Then for some minimal $m$ with $c_m \neq 0$,
\[
f(z) = \sum_{k\geq m}c_k (z-z_0)^k = (z-z_0)^m \sum_{k\geq m}c_k (z-z_0)^{k-m} \da (z-z_0)^m g(z)
,\]
where $g$ is holomorphic on some neighborhood of $z_0$ and nonvanishing at $z_0$, since $g(z_0) = c_m \neq 0$.
By continuity, $g$ is nonzero on some (potentially smaller) neighborhood $U \ni z_0$.
Since $0 = f(z_k) = = (z_k - z_0)^m g(z_k)$ for all $k$ with $z_k\neq z_0$ and $z_k$ distinct, this forces infinitely many $z_k$ to equal $z_0$, a contradiction.
So $c_m = 0$ for all $m$, forcing $f\equiv 0$.

$3\implies 1$:
Pick $z_0$ with $f^{(k)}(z_0) = 0$ for all $k$.
Then $f = \sum_{k\geq 0} c_k (z-z_0)^k$ with $c_k \sim f^{(k)}(z_0)$, so $c_k = 0$ for all $k$ and $f\equiv 0$ on some disc $D_r(z_0) \subseteq \Omega$.
Write $U \da \ts{z_0\in \Omega\st f^{(k)}(z_0) = 0 \text{ for all }k }$, then $U$ is open in $\Omega$.
The claim is that $U$ is also closed in $\Omega$, and a closed and open subset of a connected set is the entire thing.
Consider $V\da \Omega\sm U$.
If $w_0\in V$, there is some $k$ with $f^{(k)}(w_0)\neq 0$.
Since $f^{(k)}$ is continuous, it is nonzero on some neighborhood about $w_0$.
So $w_0$ is an interior point of $V$, making $V$ open and $U$ closed.

:::

:::{.proof title="?"}
![[attachments/Pasted image 20211215021255.png]]

:::

[[T-OFMGU]]

:::{.example title="?"}
Since $\sin^2(z)+\cos^2(z) = 1$ for $z\in \RR$, which has a limit point, this holds for $z\in \CC$ as well.
For the generalization, consider $F(z, w) \da e^{z+w}-e^z e^w$; then $F\equiv 0$ on $\RR$ and thus this holds on $\CC$.

:::

## Exercises

[[E-G4N4D]]
[[E-5P24A]]
