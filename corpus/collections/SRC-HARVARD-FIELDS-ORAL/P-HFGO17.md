---
schema: qual/card@1
id: P-HFGO17
kind: problem
title: A splitting field with no proper normal intermediate extension
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give a field $F$ and a polynomial $p(x)\in F[x]$ whose splitting field $E$ has no proper nontrivial intermediate extension normal over $F$.
:::

::: solution
We construct an example with
\[
\operatorname{Gal}(E/F)\cong A_5.
\]

Let $k=\mathbb Q$, introduce algebraically independent variables
\[
\{x_g:g\in A_5\},
\]
and set
\[
E=k(x_g:g\in A_5).
\]
Let $A_5$ act on $E$ by
\[
h(x_g)=x_{hg},
\]
and define the fixed field
\[
F=E^{A_5}.
\]

<1>1. The extension $E/F$ is finite Galois with
\[
\operatorname{Gal}(E/F)\cong A_5.
\]
::: proof
The action is faithful because a nonidentity $h$ sends $x_1$ to the distinct
variable $x_h$. Artin's fixed-field theorem therefore gives
\[
[E:F]=|A_5|=60
\]
and identifies the full Galois group with the acting group $A_5$.
:::

<1>2. There is a polynomial $p(x)\in F[x]$ whose splitting field is $E$.
::: proof
The extension $E/F$ is finite separable, so by the primitive element theorem
there exists $\alpha\in E$ such that
\[
E=F(\alpha).
\]
Let $p(x)$ be the minimal polynomial of $\alpha$ over $F$. Since $E/F$ is
normal, every $F$-conjugate of $\alpha$ lies in $E$, so $p$ splits in $E$.
Conversely, its roots generate the normal closure of $F(\alpha)=E$, hence its
splitting field is exactly $E$.
:::

<1>3. No proper nontrivial intermediate field $L$ with
\[
F\subsetneq L\subsetneq E
\]
is normal over $F$.
::: proof
By the Galois correspondence, $L$ corresponds to
\[
H=\operatorname{Gal}(E/L)<A_5.
\]
Because $E/F$ is Galois, the extension $L/F$ is normal if and only if $H$ is
normal in $A_5$. The group $A_5$ is simple, so its only normal subgroups are
$1$ and $A_5$, corresponding respectively to $E$ and $F$.
Therefore no proper nontrivial intermediate field is normal over $F$.
:::
:::
