---
schema: qual/card@1
id: P-GRECH7-49
kind: problem
title: Recurrence describing the $3x+1$ algorithm
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 49 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The shared algorithm lost its multiplication sign in both extractions; the solution computes 3a+1.
---

::: {.problem}
Use the algorithm for the "$3x+1$" problem:

```
input (a)
while a > 1
    begin
        if (a mod 2 = 0)
            a := a / 2
        else a := 3 * a + 1
        output (a)
    end
```

Which of the following correctly represents the algorithm described above?

(A) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_{n-1} \text{ odd} \\ 3a_{n-1} + 1 \text{ for } a_{n-1} \text{ even} \end{cases}$
(B) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_{n-1} \text{ even} \\ 3a_{n-1} + 1 \text{ for } a_{n-1} \text{ odd} \end{cases}$
(C) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_{n-1} \text{ even} \\ \frac{1}{2}(3a_{n-1} + 1) \text{ for } a_{n-1} \text{ odd} \end{cases}$
(D) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_n \text{ even} \\ 3a_{n-1} + 1 \text{ for } a_n \text{ odd} \end{cases}$
(E) $a_n = \begin{cases} \frac{1}{2}a_{n-1} \text{ for } a_n \text{ odd} \\ 3a_{n-1} + 1 \text{ for } a_n \text{ even} \end{cases}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $a_{n-1}$ is even, then the next value is
$$
a_n=\frac12 a_{n-1}.
$$


::: pf-proof

When the current value satisfies $a\bmod 2=0$, the `if` branch replaces $a$ by $a/2$. Thus an even current value $a_{n-1}$ produces $a_n=a_{n-1}/2$.

:::

:::

::: {.pf-step #s1-2}

If $a_{n-1}$ is odd, then the next value is
$$
a_n=3a_{n-1}+1.
$$


::: pf-proof

When $a_{n-1}$ is odd, the condition $a\bmod 2=0$ is false, so the `else` branch replaces $a$ by $3a+1$. Hence $a_n=3a_{n-1}+1$.

:::

:::

::: {.pf-step #s1-3}

Therefore the recurrence is
$$
\boxed{
a_n=
\begin{cases}
\frac12 a_{n-1}, & a_{n-1}\text{ even},\\
3a_{n-1}+1, & a_{n-1}\text{ odd},
\end{cases}}
$$
so the answer is (B).


::: pf-proof

Step [](#s1-1){.pf-ref} gives the even case and step [](#s1-2){.pf-ref} gives the odd case. Both branches test the parity of the current value $a_{n-1}$ before assigning the next value $a_n$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the recurrence implemented by the algorithm.

:::

:::

:::
