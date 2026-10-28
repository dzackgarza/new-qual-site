---
schema: qual/card@1
id: P-GRECH7-50
kind: problem
title: Output sequence of the $3x+1$ algorithm from $17$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 50 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The shared algorithm lost its multiplication sign in both extractions; the solution computes 3a+1.
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

What is the sequence of outputs when the input value is 17?

(A) 17, 52, 28, 14, 7, 20, 10, 5, 16, 8, 4, 2, 1
(B) 52, 28, 14, 7, 20, 10, 5, 16, 8, 4, 2, 1
(C) 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
(D) 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
(E) The sequence does not end.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Starting from $17$, the first four outputs are
$$
52,\ 26,\ 13,\ 40.
$$


::: pf-proof

The input $17$ is odd, so the algorithm first replaces it by $3(17)+1=52$ and then outputs $52$. Since $52$ and $26$ are even, the next two replacements are $52/2=26$ and $26/2=13$. Since $13$ is odd, the next replacement is $3(13)+1=40$.

:::

:::

::: {.pf-step #s1-2}

Continuing from $40$, the remaining outputs are
$$
20,\ 10,\ 5,\ 16,\ 8,\ 4,\ 2,\ 1.
$$


::: pf-proof

Successive applications of the two branches give
$$
40\mapsto20\mapsto10\mapsto5\mapsto16\mapsto8\mapsto4\mapsto2\mapsto1.
$$
Indeed, every even term is halved, while the odd term $5$ is replaced by $3(5)+1=16$. Once $1$ is output, the condition $a>1$ is false, so the loop stops.

:::

:::

::: {.pf-step #s1-3}

Hence the output sequence is
$$
\boxed{52,\ 26,\ 13,\ 40,\ 20,\ 10,\ 5,\ 16,\ 8,\ 4,\ 2,\ 1},
$$
so the answer is (D).


::: pf-proof

Concatenating the outputs from steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} gives the displayed sequence. The input $17$ itself is not output before the first iteration.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the complete sequence requested.

:::

:::

:::
