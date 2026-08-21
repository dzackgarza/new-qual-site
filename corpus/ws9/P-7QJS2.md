---
schema: qual/card@1
id: P-7QJS2
kind: problem
title: Normal families of holomorphic functions, and derivatives of a normal family
  on the disk
classification:
  areas:
  - real-analysis
  topics:
  - Normal Families
  - Holomorphic Functions
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
a. Define what is meant by a normal family of holomorphic functions on an open (possibly unbounded) domain $U$.
b. Suppose $\mathcal{F}$ is a normal family of holomorphic functions on the open unit disk $D$.
Show that the family $$\mathcal{F}' = \{f' : f \in \mathcal{F}\}$$ is also a normal family on $D$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) Define a normal family of holomorphic functions on a domain $U$; (b) show that if $\mcf$ is a normal family of holomorphic functions on the unit disk $D$, then $\mcf' = \{f' : f \in \mcf\}$ is also normal on $D$.

<1>1. (a) Definition: a family $\mcf$ of holomorphic functions on an open set $U \subseteq \CC$ is **normal** if every sequence in $\mcf$ has a subsequence that converges uniformly on every compact subset of $U$ (in the spherical metric, allowing the constant limit $\infty$). Proof: this is the standard definition.

<1>2. (b) Setup: $\mcf$ normal on $D$ implies $\mcf$ is locally bounded on $D$.
Proof: Montel's theorem for domains: a family of holomorphic functions on a domain is normal iff it is locally bounded.
(If a normal family were not locally bounded on some compact, a sequence would have a subsequence escaping to $\infty$ while another part stays bounded — violating normality; the standard statement is the cited equivalence.)

<1>3. $\mcf'$ is locally bounded on $D$.
<2>1. For any compact $K \subset D$ there is a larger compact $K' \subset D$ with $K \subset K'^\circ$ and $d = \dist(K, \bd K') > 0$.
Proof: e.g. take $K'$ a slightly enlarged closed disk (or a union of disks) inside $D$.
<2>2. For every $f \in \mcf$, $\sup_{K} |f'| \le \frac{1}{d} \sup_{K'} |f|$.
Proof: by the Cauchy estimate for derivatives on the disk centered at $z \in K$ with radius $d$ (contained in $K'$), $|f'(z)| \le \frac{1}{d} \max_{|w - z| \le d}|f(w)| \le \frac{1}{d} \sup_{K'}|f|$; take the supremum over $z \in K$.
<2>3. $\sup_{f \in \mcf} \sup_K |f'| < \infty$.
Proof: $\sup_{K'}|f| \le M_{K'} < \infty$ for all $f$ by local boundedness (<1>2), so <2>2 gives the uniform bound $M_{K'}/d$ on $K$.

<1>4. $\mcf'$ is normal on $D$.
Proof: by Montel's theorem again (<1>2), local boundedness (<1>3) implies normality.

<1>5. Q.E.D. Proof: <1>1 answers (a) and <1>2–<1>4 prove (b).
:::
