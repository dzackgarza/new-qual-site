---
schema: qual/card@1
id: E-MUN-10-9
kind: problem
title: Antidictionary order on sequences ending in $1$'s
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Consider the subset $A$ of $(\mathbb{Z}_{+})^{\omega}$ consisting of all infinite sequences of positive integers $\mathbf{x} = (x_{1}, x_{2}, \ldots)$ that end in an infinite string of 1's. Give $A$ the following order: $\mathbf{x} < \mathbf{y}$ if $x_{n} < y_{n}$ and $x_{i} = y_{i}$ for $i > n$ . We call this the "antidictionary order" on $A$ .

(a) Show that for every $n$, there is a section of $A$ that has the same order type as $(\mathbb{Z}_+)^n$ in the dictionary order.

(b) Show $A$ is well-ordered.
:::

::: {.solution}
Let \(A_n\subset A\) denote the set of sequences whose coordinates after the \(n\)-th are all \(1\).

For part (a), put
\[
s^{(n)}=(\underbrace{1,\ldots,1}_{n\text{ entries}},2,1,1,\ldots).
\]
Then the section
\[
A_{<s^{(n)}}=\{x\in A:x<s^{(n)}\}
\]
is exactly \(A_n\). Indeed, if \(x<s^{(n)}\), at the largest coordinate where the two sequences differ one cannot be beyond \(n+1\), since there \(s^{(n)}\) has value \(1\); at coordinate \(n+1\) the inequality forces \(x_{n+1}=1<2\), and all later coordinates are \(1\). Conversely every element of \(A_n\) is \(<s^{(n)}\).

Define
\[
\phi_n:A_n\longrightarrow (\mathbb Z_+)^n,
\qquad
\phi_n(x_1,\ldots,x_n,1,1,\ldots)=(x_n,x_{n-1},\ldots,x_1).
\]
This is a bijection. In the antidictionary order, two elements of \(A_n\) are compared at their largest differing coordinate; after reversing the first \(n\) coordinates, this becomes the first differing coordinate. Hence \(\phi_n\) is an order isomorphism onto \((\mathbb Z_+)^n\) with dictionary order.

For part (b), first note by induction on \(n\) that \((\mathbb Z_+)^n\) in dictionary order is well ordered. The case \(n=1\) is the usual well ordering of \(\mathbb Z_+\). If the assertion holds for \(n\), then for a nonempty subset \(B\subset(\mathbb Z_+)^{n+1}\), choose the least first coordinate occurring in \(B\), and within that fiber choose the least remaining \(n\)-tuple.

Now let \(B\subset A\) be nonempty and choose \(b\in B\). Since \(b\) is eventually \(1\), there is \(n\) with \(b\in A_n\). Every \(x<b\) also lies in \(A_n\): if \(x\) differed from \(b\) at some coordinate \(m>n\), then \(b_m=1\), while \(x_m\ge1\), so the required inequality \(x_m<b_m\) at the largest differing coordinate would be impossible. Therefore
\[
B\cap(-\infty,b]\subset A_n.
\]
This set is nonempty and, by part (a), lies in a well-ordered set, so it has a least element \(b_0\). If \(x\in B\) and \(x<b_0\), then \(x<b\) as well and hence \(x\in B\cap(-\infty,b]\), contradicting the minimality of \(b_0\). Thus \(b_0\) is the least element of \(B\). Hence \(A\) is well ordered.
:::
