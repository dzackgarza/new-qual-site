---
schema: qual/card@1
id: P-FOU3L
kind: problem
title: Invertibility outside $\langle p\rangle$ and purity in $\langle p\rangle$-primary modules over a PID
classification:
  areas:
  - algebra
  topics:
  - modules
  - primary-decomposition
  - principal-ideal-domains
relations: []
review: draft
solved: true
---

::: problem
Let $R$ be a PID and $M$ be an $R\dash$module.
Let $p$ be a prime element of $R$.
The module $M$ is called *$\generators{p}\dash$primary* if for every $m \in M$ there exists $k > 0$ such that $p^k m = 0$.

a. Suppose M is $\generators{p}\dash$primary.
Show that if $m \in M$ and $t \in R, ~t \not\in \generators{p}$, then there exists $a \in R$ such that $atm = m$.

b. A submodule $S$ of $M$ is said to be *pure* if $S \cap r M = rS$ for all $r \in R$.
Show that if $M$ is $\generators{p}\dash$primary, then $S$ is pure if and only if $S \cap p^k M = p^k S$ for all $k \geq 0$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Existence of $a \in R$ such that $atm = m$:** Since $M$ is $\langle p \rangle$-primary, there exists an integer $k > 0$ such that $p^k m = 0$.
Since $R$ is a PID, every prime element is irreducible.
Because $p \nmid t$, we have $\gcd(t, p^k) = 1$.
By Bézout's identity in the PID $R$, there exist elements $a, b \in R$ such that:
$$
at + b p^k = 1.
$$
Multiplying both sides by $m$ (using the module action):
$$
(at + b p^k) m = 1 \cdot m \implies a t m + b(p^k m) = m.
$$
Since $p^k m = 0$, we obtain $atm + 0 = m$, so $atm = m$.

**(b) Characterization of purity for $\langle p \rangle$-primary modules:**

The forward direction ($\implies$) is immediate by setting $r = p^k$.

For the reverse direction ($\Longleftarrow$): Assume $S \cap p^k M = p^k S$ for all $k \geq 0$.
Let $r \in R$.
If $r = 0$, $S \cap 0M = 0 = 0S$, which holds.
So assume $r \neq 0$.
Since $R$ is a PID (hence a UFD), we can factor $r$ as:
$$
r = u p^k t,
$$
where $u \in R^\times$ is a unit, $k \geq 0$, and $t \in R$ satisfies $\gcd(t, p) = 1$, i.e. $t \notin \langle p \rangle$.
Note that multiplying by a unit preserves submodules, so $r M = p^k t M$ and $r S = p^k t S$.

We always have $rS \subseteq S \cap rM$.
To show $S \cap rM \subseteq rS$: Let $s \in S \cap rM$.
Then $s = rm = u p^k t m$ for some $m \in M$.
In particular, $s = p^k(u t m) \in p^k M$.
Since $s \in S$, we have $s \in S \cap p^k M$.
By our hypothesis for $p^k$, $S \cap p^k M = p^k S$.
Thus, there exists $s' \in S$ such that:
$$
s = p^k s'.
$$
Now, consider $s' \in S$.
Since $M$ is $\langle p \rangle$-primary, $S$ is also $\langle p \rangle$-primary.
Since $t \notin \langle p \rangle$, by part (a) there exists $a \in R$ such that:
$$
a t s' = s'.
$$
Therefore:
$$
s = p^k s' = p^k (a t s') = p^k t (a s') = (u^{-1} r) (a s') = r (u^{-1} a s').
$$
Since $s' \in S$ and $S$ is an $R$-submodule, $u^{-1} a s' \in S$.
Hence $s \in rS$.

This proves $S \cap rM = rS$ for all $r \in R$, so $S$ is pure.
:::
