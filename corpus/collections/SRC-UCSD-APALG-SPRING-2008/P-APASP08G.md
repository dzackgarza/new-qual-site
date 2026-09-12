---
schema: qual/card@1
id: P-APASP08G
kind: problem
title: "Symmetric function identity involving hooks"
classification:
  areas:
  - applied-algebra
  topics:
  - Symmetric Functions
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Show that
$$
e^{t p_1} = \sum_\lambda t^{|\lambda|}\frac{s_\lambda}{h_\lambda},
$$
where $h_\lambda$ denotes the product of the hook lengths of $\lambda$.
:::

::: solution
Since $p_1=s_{(1)}$, repeated application of the Pieri rule gives
\[
p_1^n=s_{(1)}^n=\sum_{\lambda\vdash n} f^\lambda s_\lambda,
\]
where $f^\lambda$ is the number of standard Young tableaux of shape $\lambda$.
Indeed, multiplying by $s_{(1)}$ adds one box, and a sequence of $n$ successive legal box additions from the empty partition to $\lambda$ is exactly a standard Young tableau of shape $\lambda$.

By the hook-length formula,
\[
f^\lambda=\frac{n!}{h_\lambda},
\]
where
\[
h_\lambda=\prod_{u\in\lambda} h(u)
\]
is the product of the hook lengths of all boxes of $\lambda$. Therefore
\[
p_1^n
=
\sum_{\lambda\vdash n}\frac{n!}{h_\lambda}s_\lambda.
\]
Now expand the exponential:
\[
\begin{aligned}
e^{tp_1}
&=\sum_{n\ge0}\frac{t^n p_1^n}{n!}\\
&=\sum_{n\ge0}\frac{t^n}{n!}
\sum_{\lambda\vdash n}\frac{n!}{h_\lambda}s_\lambda\\
&=\sum_{n\ge0}\sum_{\lambda\vdash n}
 t^n\frac{s_\lambda}{h_\lambda}\\
&=\sum_\lambda t^{|\lambda|}\frac{s_\lambda}{h_\lambda}.
\end{aligned}
\]
Hence
\[
\boxed{
e^{tp_1}=
\sum_\lambda t^{|\lambda|}\frac{s_\lambda}{h_\lambda}.
}
\]
:::
