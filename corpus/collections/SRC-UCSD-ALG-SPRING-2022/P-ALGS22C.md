---
schema: qual/card@1
id: P-ALGS22C
kind: problem
title: "Determining module structure from rank and fiber dimensions over a PID"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $R$ be a PID and let $M$ be a finitely generated $R$-module. Let $K$ be the field of
fractions of $R$.

Suppose that you do not know $M$ but are given the value of $\dim_K(M \otimes_R K)$ as
well as $\dim_{R/\mathfrak{m}}(M \otimes_R (R/\mathfrak{m}))$ for each maximal ideal
$\mathfrak{m}$ of $R$. Which of the following can you determine precisely from this
information? If the data can be determined, explain how, and if not, give 2 examples of
$M$ to show that the calculation is ambiguous.

(a) The rank of $M$.

(b) The number of elementary divisors of $M$ that are powers of a given prime $p$.

(c) The exact list of elementary divisors of $M$.
:::

::: {.solution}
<1>1. By the structure theorem for finitely generated modules over a PID, write
\[
M\cong R^r\oplus\bigoplus_{q}\bigoplus_{j=1}^{s_q}R/(q^{e_{q,j}}),
\]
where \(q\) runs over primes of \(R\), up to associates, and every \(e_{q,j}\ge1\).
::: {.proof}
This is the elementary-divisor form of the structure theorem for finitely generated
modules over a PID.
:::

<1>2. The supplied number \(\dim_K(M\otimes_RK)\) is exactly
\(r=\operatorname{rank}_R M\). Thus part (a) is determined precisely.
::: {.proof}
Tensoring with \(K\) kills every torsion summand and sends \(R^r\) to \(K^r\). Hence
\[
M\otimes_RK\cong K^r.
\]
:::

<1>3. Fix a prime \(p\), and let \(\mathfrak m=(p)\). Then
\[
\dim_{R/(p)}(M\otimes_RR/(p))=r+s_p.
\]
::: {.proof}
The free summand contributes \((R/(p))^r\). For a torsion summand \(R/(q^e)\),
\[
R/(q^e)\otimes_RR/(p)\cong R/(q^e,p).
\]
If \(q\) is not associate to \(p\), then \((q^e,p)=R\), so this tensor product is zero.
If \(q\) is associate to \(p\), then \((p^e,p)=(p)\), so the tensor product is
\(R/(p)\), independently of \(e\). Thus exactly the \(s_p\) elementary divisors that are
powers of \(p\) contribute one dimension each.
:::

<1>4. Therefore part (b) is determined precisely by
\[
s_p=\dim_{R/(p)}(M\otimes_RR/(p))-\dim_K(M\otimes_RK).
\]
::: {.proof}
Subtract the value \(r\) found in <1>2 from the identity in <1>3.
:::

<1>5. Part (c) is not determined by the supplied data.
::: {.proof}
Take
\[
M_1=R/(p),\qquad M_2=R/(p^2).
\]
Both have rank zero. For the maximal ideal \((p)\), both fibers are one-dimensional over
\(R/(p)\); for every maximal ideal \((q)\neq(p)\), both fibers vanish. Hence all
supplied dimensions are identical for \(M_1\) and \(M_2\). Nevertheless their
elementary-divisor lists are respectively \(\{p\}\) and \(\{p^2\}\), so the exact
exponents cannot be recovered.
:::

<1>6. Hence (a) and (b) can be determined precisely, while (c) cannot.
::: {.proof}
Combine <1>2, <1>4, and <1>5.
:::
:::
