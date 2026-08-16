---
schema: qual/card@1
id: P-SBXGZ
kind: problem
title: Let $R$ be a commutative ring, and let $M$ be an $R\dash$module. An...
classification:
  areas:
  - algebra
  topics:
  - modules
  - maximal-ideals
  - roots-of-unity
relations: []
review: draft
---

::: problem
Let $R$ be a commutative ring, and let $M$ be an $R\dash$module.
An $R\dash$submodule $N$ of $M$ is maximal if there is no $R\dash$module $P$ with $N \subsetneq P \subsetneq M$.

(a) Show that an $R\dash$submodule $N$ of $M$ is maximal $\iff M /N$ is a simple $R\dash$module: i.e., $M /N$ is nonzero and has no proper, nonzero $R\dash$submodules.

(b) Let $M$ be a $\ZZ\dash$module.
Show that a $\ZZ\dash$submodule $N$ of $M$ is maximal $\iff \#M /N$ is a prime number.

(c) Let $M$ be the $\ZZ\dash$module of all roots of unity in $\CC$ under multiplication.
Show that there is no maximal $\ZZ\dash$submodule of $M$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) $N$ is maximal $\iff M/N$ is simple:**
By the Lattice (Correspondence) Theorem for modules, there is an inclusion-preserving bijection between the $R$-submodules of $M$ containing $N$ and the $R$-submodules of the quotient module $M/N$, given by:
$$
P \longleftrightarrow P/N.
$$
- $N$ is a maximal proper submodule of $M$ if and only if $N \subsetneq M$ (so $M/N \neq 0$) and the only submodules $P$ of $M$ containing $N$ are $P = N$ and $P = M$.
- Under the correspondence, this occurs if and only if the only submodules of $M/N$ are $N/N = \{0\}$ and $M/N$.
- A non-zero module with no proper non-zero submodules is precisely a **simple module**.
Thus $N$ is maximal $\iff M/N$ is simple.

**(b) For a $\ZZ$-module, $N$ is maximal $\iff \#(M/N)$ is prime:**
A $\ZZ$-module is simply an abelian group, and submodules are subgroups.
By part (a), $N$ is maximal if and only if $S = M/N$ is a simple $\ZZ$-module (a simple abelian group).
- **If $\#(M/N) = p$ (a prime):** Any group of prime order has no proper non-trivial subgroups, so $M/N$ is simple, hence $N$ is maximal.
- **Conversely, let $S = M/N$ be simple:** Pick any non-zero element $x \in S \setminus \{0\}$.
  The cyclic subgroup $\langle x \rangle = \ZZ x$ is a non-zero submodule of $S$. Since $S$ is simple, $\langle x \rangle = S$, so $S$ is cyclic: $S \cong \ZZ / k\ZZ$ for some $k \geq 0$.
  - If $k = 0$ (so $S \cong \ZZ$), then $2\ZZ \subsetneq \ZZ$ is a proper non-zero submodule, so $\ZZ$ is not simple.
  - If $k \geq 1$ is composite with non-trivial factorization $k = ab$ ($a, b > 1$), then $a(\ZZ/k\ZZ) \cong \ZZ/b\ZZ$ is a proper non-zero submodule, so $\ZZ/k\ZZ$ is not simple.
  - Thus $k = p$ must be a prime number, which means $\#(M/N) = p$.

**(c) Roots of unity $\mu_\infty \subset \CC^\times$ has no maximal $\ZZ$-submodule:**
The group $M = \mu_\infty = \{z \in \CC \mid z^n = 1 \text{ for some } n \geq 1\}$ under multiplication is isomorphic (as an abelian group / $\ZZ$-module) to the Prüfer quotient $\QQ/\ZZ$.

Suppose towards a contradiction that $N \subsetneq M$ is a maximal submodule.
By part (b), the quotient $M/N$ has prime order $p$.
This means that for every $x \in M$, $x^p \in N$ (in multiplicative notation).
Therefore, $M^p = \{z^p \mid z \in M\} \subseteq N$.

However, the group of roots of unity $M = \mu_\infty$ is **divisible**:
For every $w \in M$ and every integer $p \geq 1$, there exists $z \in M$ such that $z^p = w$ (since if $w^n = 1$, then $z = e^{2\pi i k / (pn)}$ satisfies $z^p = w$ and $z^{pn} = 1$).
Therefore:
$$
M^p = M.
$$
This implies $M = M^p \subseteq N \subsetneq M$, a contradiction ($M \subseteq N$).
Thus, $M$ has no maximal $\ZZ$-submodules.
:::
