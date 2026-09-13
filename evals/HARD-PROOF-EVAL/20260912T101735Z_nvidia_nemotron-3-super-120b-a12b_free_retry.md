# Retry Eval: nvidia/nemotron-3-super-120b-a12b:free

- Original run: 20260912T085503Z
- Retry timestamp (UTC): 20260912T101735Z
- Model timestamp (UTC): 20260912T103430Z
- Model: `nvidia/nemotron-3-super-120b-a12b:free`
- Provider: `nvidia`
- Success: True
- Usage: {"prompt_tokens": 3646, "completion_tokens": 25508, "total_tokens": 29154, "cost": 0, "is_byok": false, "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0, "audio_tokens": 0, "video_tokens": 0}, "cost_details": {"upstream_inference_cost": 0, "upstream_inference_prompt_cost": 0, "upstream_inference_completions_cost": 0}, "completion_tokens_details": {"reasoning_tokens": 15596, "image_tokens": 0, "audio_tokens": 0}}
- Problem source: `HARD-PROOF-EVAL.md` verbatim
- Prompt length: 8778 chars
- Max tokens: per-model saturated (235929), timeout: none, spaced 15s

---

## Chain-of-Thought (reasoning)

We need to produce a full solution with proofs for each part (a)-(g). The problem statement is given. The solution skeleton is provided in the prompt, but we need to flesh out details, ensure rigorous reasoning, fill any gaps, and present a complete answer.

We need to show:

(a) No uniform r exists without further restrictions. Provide sequence f_n(z)=z/n, compute f_n'(0)=1/n, show 1/n not in image, etc.

(b) Even with f'(0)=1, no uniform r exists. Use f_epsilon(z)=epsilon(e^{z/epsilon} -1). Show f_epsilon(0)=0, f_epsilon'(0)=1, image omits -epsilon, so for any r>0 choose epsilon<r then -epsilon in D_r(0) but not in image.

(c) For h(z)=1/z + c0 + c1 z + ... injective on punctured disc 0<|z|<1, show sum_{n>=1} n|c_n|^2 <=1. Use area theorem (Gronwall's area theorem). Compute area of complement of h(D_rho\{0}) and let rho->1.

We need to provide proof: For injective meromorphic function on punctured disc with simple pole at 0, the area of complement of image of {0<|z|<rho} is pi(1/rho^2 - sum_{n>=1} n|c_n|^2 rho^{2n}) >=0. Then letting rho->1 gives inequality.

(d) Given f(z)=z + a2 z^2 + ... injective, f(0)=0, f'(0)=1. Show there exists g injective with same normalization such that g^2(z)=f(z^2). Approach: Since f(z)/z is nowhere zero and holomorphic on D, we can define a holomorphic square root psi with psi(0)=1 (since f(z)/z = 1 + a2 z + ... nonzero at 0). Then define g(z)=z psi(z^2). Show g is injective, g(0)=0, g'(0)=1, and g^2(z)=f(z^2).

(e) Using previous, show |a2| <=2, equality iff f(z)=z/(1 - e^{i theta}z)^2. Steps: Compute expansion of 1/g(z) = 1/z + b0 + b1 z + ...; note g is odd so only odd powers; relate b1 to a2; apply part (c) to 1/g to get |b1| <=1; then |a2|=2|b1| <=2. Equality case: if |b1|=1 then equality in area theorem forces 1/g(z)=1/z + e^{i theta} z, thus g(z)=z/(1+ e^{i theta} z^2). Then compute f(z)=g(z)^2 with substitution z-> sqrt? Actually we have g^2(z)=f(z^2). So f(z)= (g(sqrt(z)))^2? Wait careful: we have g^2(z) = f(z^2). So for any w, f(w) = g(sqrt(w))^2 where sqrt denotes a branch; but since both sides are even? Actually we can deduce: replace z by sqrt(z) (choose principal branch) yields f(z) = g(sqrt(z))^2. But we can also directly compute: from g(z)=z psi(z^2) and psi^2(z)=f(z)/z, we have g(z)=z sqrt{f(z)/z}? Actually psi(z) = sqrt{f(z)/z}. Then g(z) = z psi(z^2) = z sqrt{f(z^2)/z^2} = sqrt{f(z^2)}. Wait check: psi(z^2) = sqrt{f(z^2)/z^2}. Multiply by z: g(z) = z * sqrt{f(z^2)/z^2} = sqrt{f(z^2)}. So g(z)^2 = f(z^2). Good. Then if g(z) = z/(1+ e^{i theta} z^2), then g(z)^2 = z^2/(1+ e^{i theta} z^2)^2. So f(z^2) = z^2/(1+ e^{i theta} z^2)^2. Replace w = z^2: f(w) = w/(1+ e^{i theta} w)^2. So indeed f(z)=z/(1+ e^{i theta} z)^2.

Equality case also includes rotation.

(f) If h injective on D and avoids two values z1, z2, then |z1 - z2| <=4. Approach: Consider 1/(h(z)-z_j) which is injective, has simple pole at 0, expansion 1/z + ... ; apply part (c) to get bound on coefficient of z term; relate difference of coefficients to z1 - z2; get bound.

We need to be precise: Let h(z) injective on D, avoid z1 and z2. Then for each j, define H_j(z) = 1/(h(z)-z_j). Since h avoids z_j, denominator never zero, H_j is holomorphic on D. Moreover, H_j has a simple pole at 0? Actually h(0) may be something; but we can assume after translation that h(0)=0? The statement likely assumes h is injective on D and avoids z1, z2, but not necessarily normalized. However we can apply part (c) after subtracting a constant to make pole at 0? Usually the area theorem applies to functions of form 1/z + c0 + c1 z + ... which are injective on punctured disc. So we need to ensure H_j has that form. Since h is injective on D, h(0) is some value; but we can consider H_j(z) - 1/z? Actually we need to get expansion at 0: Since h is injective and avoids z_j, h(z)-z_j is nonzero and holomorphic, with a zero at some point? Wait h may not have zero at 0. But we can consider the function 1/(h(z)-z_j) which is holomorphic and nonzero? Actually if h avoids z_j, then h(z)-z_j never zero, so its reciprocal is holomorphic and nonzero? No, it's holomorphic and never zero, but may have a zero at infinity? Not needed. To get a simple pole at 0, we need h(z)-z_j to have a simple zero at 0. So we need to assume h(0)=z_j? That seems not given. However typical proof of Koebe 1/4 theorem uses that if f omits w, then 1/f omits 0 and 1/w, and 1/f has a simple pole at 0 because f(0)=0 and f'(0)=1 => near 0, f(z)=z+..., so 1/f(z)=1/z + ... . So in part (f) we likely consider h injective on D and avoids z1, z2, and also h(0)=0? Actually the statement: "If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, show that |z1 - z2| <= 4." Wait they already gave the form of h: h(z) = 1/z + c0 + c1 z + ... . So h already has a simple pole at 0 with residue 1. So they assume h is of that form (i.e., meromorphic on D with simple pole at 0, residue 1). And h is injective on D (including at 0? Actually it's meromorphic, injective as a map from D\{0} to C). So we can directly apply part (c) to h and to h - (z1+z2)/2? Hmm.

But the hint: "Look at the second coefficient in the power series expansion of 1/(h(z) - z_j)." So we consider H_j(z) = 1/(h(z) - z_j). Since h has pole at 0, h(z)-z_j also has pole at 0 (same principal part). Its reciprocal then has a zero at 0? Let's compute: If h(z) = 1/z + c0 + c1 z + ..., then near 0, h(z)-z_j = 1/z + (c0 - z_j) + c1 z + ... . Its reciprocal: 1/(h(z)-z_j) = z / [1 + (c0 - z_j) z + c1 z^2 + ...] = z * [1 - (c0 - z_j) z + ...] = z - (c0 - z_j) z^2 + ... . So expansion: H_j(z) = z + d0 + d1 z + ...? Actually we see that H_j(z) has a zero at 0 (no pole). Its expansion starts with z term. So it's holomorphic at 0 with zero of order 1. Then we can consider K_j(z) = 1/H_j(z) = h(z)-z_j, which has pole at 0. But part (c) applies to functions with simple pole at 0 and residue 1. So we might instead consider 1/H_j(z) = h(z)-z_j, which has pole at 0 but residue 1? Let's check: h(z)-z_j = 1/z + (c0 - z_j) + c1 z + ... . So indeed it has simple pole at 0 with residue 1. So h(z)-z_j is of the form required in part (c). And it's injective? Since h is injective and subtracting constant z_j doesn't affect injectivity, h(z)-z_j is injective on D\{0}. So we can apply part (c) to the function h(z)-z_j. Then we get sum_{n>=1} n|d_n|^2 <= 1 where d_n are coefficients in expansion of h(z)-z_j = 1/z + d0 + d1 z + d2 z^2 + ... . Here d0 = c0 - z_j, d1 = c1, etc. So the bound applies to the coefficients d_n for n>=1: sum n|d_n|^2 <=1. In particular, |d1| <=1. So |c1| <=1 for each j? Wait d1 = c1 (since subtracting constant doesn't affect z coefficient). So we get |c1| <=1. That seems too weak to get |z1 - z2| <=4. Actually we need to use both j=1,2 to get bound on difference.

Maybe we consider the difference of the two functions: (h(z)-z1) - (h(z)-z2) = z2 - z1, constant. Not helpful.

Alternate approach: Consider the function H(z) = 1/(h(z)-z1) - 1/(h(z)-z2). This equals (z2 - z1)/[(h(z)-z1)(h(z)-z2)]. Might be easier to bound.

But hint says: Look at second coefficient in power series expansion of 1/(h(z)-z_j). So they consider expansion of 1/(h(z)-z_j) around 0. As we computed, 1/(h(z)-z_j) = z - (c0 - z_j) z^2 + ... . So the coefficient of z^2 is -(c0 - z_j). The second coefficient (maybe meaning coefficient of z) is 1? Actually series: a_{-1}? Wait they'd write expansion in powers of z: 1/(h(z)-z_j) = A_{-1} z^{-1} + A_0 + A_1 z + ...? But we found it's holomorphic at 0, so no negative powers. Let's recompute carefully:

h(z) = 1/z + c0 + c1 z + c2 z^2 + ...

Then h(z) - z_j = 1/z + (c0 - z_j) + c1 z + c2 z^2 + ...

We want to compute its reciprocal: 1/(h(z)-z_j). Let w = h(z)-z_j. Write w = (1/z) * [1 + (c0 - z_j) z + c1 z^2 + c2 z^3 + ...]. So w = (1/z) * (1 + alpha_1 z + alpha_2 z^2 + ...), where alpha_1 = c0 - z_j, alpha_2 = c1, etc.

Then 1/w = z * (1 + alpha_1 z + alpha_2 z^2 + ...)^{-1} = z * [1 - alpha_1 z + (alpha_1^2 - alpha_2) z^2 + ...].

Thus 1/(h(z)-z_j) = z - alpha_1 z^2 + (alpha_1^2 - alpha_2) z^3 + ... .

So expansion: = z + b0 + b1 z + b2 z^2 + ...? Actually there is no constant term; the series starts with z term. So we can write:

1/(h(z)-z_j) = z + A_0 + A_1 z + A_2 z^2 + ...? Wait that seems off: If we factor z, we have z * (1 + A_1 z + A_2 z^2 + ...). So the series is z + A_1 z^2 + A_2 z^3 + ... . So there is no term independent of z (i.e., z^0). So the coefficient of z^0 is 0. The coefficient of z^1 is 1. The coefficient of z^2 is A_1 = -(c0 - z_j). The coefficient of z^3 is A_2 = (c0 - z_j)^2 - c1, etc.

Thus the "second coefficient" likely refers to the coefficient of z^2 (i.e., the coefficient after the leading term). So that coefficient is -(c0 - z_j). Then applying part (c) to the function 1/(h(z)-z_j) ??? But part (c) applies to functions of form 1/z + c0 + c1 z + ... injective on punctured disc. However 1/(h(z)-z_j) is holomorphic at 0 (has a zero), not of that form. So we cannot directly apply (c). Instead we might consider its reciprocal, which is h(z)-z_j, which is of the right form. Then the coefficient of z in h(z)-z_j is c1. So applying (c) gives |c1| <= 1. That doesn't involve z_j.

Thus we need a different approach: Maybe we consider the function H(z) = 1/(h(z)-z1) + 1/(h(z)-z2). Its expansion might give something like 2/z + ... and then apply (c) to get bound on something like (z1+z2). Hmm.

Let's recall known proof of Koebe 1/4 theorem: If f omits w, then consider F(z) = 1/f(z) - 1/w. This function omits 0 and -1/w? Actually standard proof: Suppose f omits w ≠ 0. Then g(z) = w f(z)/(w - f(z)) is univalent, normalized, and omits 0. Then apply area theorem to g'(z) or something. Another approach: Use that if f omits w, then the function h(z) = 1/f(z) - 1/w is univalent and omits 0 and something, then apply area theorem to get bound on |w|.

But the problem's part (f) is a lemma: If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, then |z1 - z2| <= 4. This is a known result: If a univalent function on the unit disk (with normalization 1/z + ... ) omits two values, then the distance between those omitted values is at most 4. This is used to prove Koebe 1/4: If f omits w, then 1/f omits 0 and 1/w, apply the lemma with z1=0, z2=1/w to get |1/w| <= 4 => |w| >= 1/4.

Thus we need to prove the lemma. Let's attempt to prove it.

Let h(z) = 1/z + c0 + c1 z + c2 z^2 + ... be injective on D (i.e., univalent on D\{0}? Actually h is meromorphic with simple pole at 0, injective on D). Suppose h omits two distinct values a and b (I'll use z1, z2). Consider the function

H(z) = \frac{1}{h(z) - a} - \frac{1}{h(z) - b}.

Compute H(z) = \frac{b - a}{(h(z)-a)(h(z)-b)}.

Since h omits a and b, denominator never zero, so H is holomorphic on D. Moreover, as z→0, h(z) ~ 1/z, so h(z)-a ~ 1/z, h(z)-b ~ 1/z, thus product ~ 1/z^2, so H(z) ~ (b-a) z^2. So H has a zero of order at least 2 at z=0. Actually we can compute expansion: h(z) = 1/z + c0 + c1 z + ...; then

1/(h(z)-a) = z - (c0 - a) z^2 + O(z^3)
1/(h(z)-b) = z - (c0 - b) z^2 + O(z^3)

Subtract: H(z) = [(c0 - b) - (c0 - a)] z^2 + O(z^3) = (a - b) z^2 + O(z^3). So H(z) = (a - b) z^2 + higher order.

Thus H(z)/z^2 is holomorphic at 0 with value (a - b) at 0.

Now consider the function G(z) = H(z)/z^2. Then G is holomorphic on D, G(0) = a - b.

We want to bound |a - b| using area theorem applied to something like 1/G? Not sure.

Alternatively, consider the function

F(z) = \frac{1}{h(z) - a} + \frac{1}{h(z) - b}.

Its expansion: sum = 2z - (2c0 - a - b) z^2 + O(z^3). So F(z)/z = 2 - (2c0 - a - b) z + ... . So F(z)/z is holomorphic, nonzero at 0? Its value at 0 is 2.

Maybe we can apply area theorem to the function

\phi(z) = \frac{1}{F(z)} ?

Let's think: We want to bound |a-b|. Known proof: If h omits a and b, then consider the function

\phi(z) = \frac{h(z) - a}{h(z) - b}.

This maps D into C \ {0,1} (since h omits a,b, the ratio never equals 0 or ∞? Actually if h(z) = a then numerator zero => ratio 0, but h omits a so numerator never zero; if h(z) = b then denominator zero => ratio ∞, but h omits b so denominator never zero; thus ratio omits 0 and ∞, i.e., takes values in C\{0,∞} = C*? Actually omitting 0 and ∞ means it's nonzero and finite, i.e., maps into C\{0}. But also it never equals 1? If h(z) = something else? Actually ratio =1 when h(z)-a = h(z)-b => a=b, which is false. So ratio never equals 1 either? Wait solve (h-a)/(h-b)=1 => h-a = h-b => -a = -b => a=b, contradiction. So ratio omits 1 as well. So the ratio omits three values: 0,1,∞. By Picard's theorem, a meromorphic function on D omitting three values is constant. But h is not necessarily meromorphic on whole D? It is meromorphic with a pole at 0, but ratio may be analytic? Let's check: (h-a)/(h-b) is meromorphic on D, with possible poles where h=b (but h omits b, so no poles), zeros where h=a (but h omits a, so no zeros). So it's holomorphic and nonzero on D. Moreover, as z→0, h(z) ~ 1/z, so (h-a)/(h-b) ~ (1/z)/(1/z) = 1. So it tends to 1 at 0. So it's a holomorphic function on D that never takes values 0,1,∞ (i.e., never 0 or 1, and finite nonzero). Actually it's holomorphic and never 0, and its reciprocal is also holomorphic (since never ∞). So it's a holomorphic map from D to C\{0,1}. By Picard's little theorem, a holomorphic function from D to C omitting two values is constant. Here we omit 0 and 1, so it must be constant. Since its limit at 0 is 1, the constant must be 1. Therefore (h-a)/(h-b) ≡ 1, implying a=b, contradiction unless the omitted values are not distinct. Wait this suggests that a meromorphic function on D omitting three values must be constant, but we only omitted two values (0 and 1) for the ratio; we also omitted ∞ implicitly because it's holomorphic (no poles). So indeed we omitted three values: 0,1,∞. So by Picard, the ratio is constant. Since limit at 0 is 1, constant =1, giving a=b. So if h omits two distinct values a,b, then the ratio (h-a)/(h-b) is a holomorphic function on D omitting 0,1,∞, thus constant, leading to a=b. Therefore h cannot omit two distinct values unless it's constant? But h is not constant because it has a pole at 0. Something is off: The ratio (h-a)/(h-b) is holomorphic on D? Let's check: h is meromorphic with a simple pole at 0. At z=0, h has a pole, so h-a and h-b also have poles. Their ratio near 0: (1/z + ... - a)/(1/z + ... - b) = (1/z (1 + (c0 - a)z + ...))/(1/z (1 + (c0 - b)z + ...)) = (1 + (c0 - a)z + ...)/(1 + (c0 - b)z + ...). This is holomorphic at 0 and equals 1 at z=0. So indeed the ratio extends holomorphically to 0. So the ratio is holomorphic on all of D. It never takes value 0 because numerator never zero (h omits a). It never takes value ∞ because denominator never zero (h omits b). It never takes value 1 because that would imply a=b. So it omits three values 0,1,∞. By Picard's theorem, a holomorphic function on D omitting three values is constant. Since its value at 0 is 1, it's identically 1. Therefore (h-a)/(h-b) ≡ 1 => h-a ≡ h-b => a=b. So indeed a non-constant meromorphic function on D with a simple pole at 0 cannot omit two distinct values. Wait but we know the Koebe function omits -1/4 only one value. So indeed it cannot omit two values. This seems to prove that if h omits two values, then it must be constant, which contradicts the pole. Therefore the lemma statement "If h is injective on D and avoids the values z1 and z2, then |z1 - z2| <= 4" is vacuously true? Actually if h omits two values, then it must be constant, which cannot happen because of the pole, so the hypothesis cannot be satisfied unless the omitted values are equal? But the lemma likely intends that h omits the values z1 and z2 (i.e., does not take those values) but may still be non-constant; the conclusion is that the distance between them is at most 4. This is a known result: If a univalent function on the unit disk (with normalization f(z)=z+... ) omits two values, then those values lie within distance 4 of each other. Actually the standard lemma: If f is univalent in D and omits the values a and b, then |a-b| ≤ 4. This is used in the proof of Koebe 1/4 theorem via considering g(z) = f(z)/(f(z)-w) etc. Wait I recall a lemma: If f is univalent in D and f(0)=0, f'(0)=1, and f omits w, then |w| ≥ 1/4. The proof uses the function F(z) = z f'(z)/(f(z)-w). Something like that.

But the problem's part (f) is stated as: If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, then |z1 - z2| ≤ 4. The hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j). So they want to use part (c) on the functions 1/(h(z)-z_j). Let's try to make that work.

Let H_j(z) = 1/(h(z)-z_j). As we computed, H_j(z) = z - (c0 - z_j) z^2 + O(z^3). So H_j(z) is holomorphic on D, with a zero at 0 of order 1 (since leading term z). So we can consider the function K_j(z) = H_j(z)/z = 1 - (c0 - z_j) z + O(z^2). This is holomorphic and nonzero at 0 (value 1). Then we can apply part (c) to something like 1/K_j? Actually 1/K_j(z) = z/H_j(z) = h(z)-z_j, which has the form 1/z + (c0 - z_j) + c1 z + ... . So 1/K_j(z) is of the form required in part (c). And it's injective? Since h is injective, subtracting constant doesn't affect injectivity, so h(z)-z_j is injective on D\{0}. So we can apply part (c) to the function h(z)-z_j. That yields sum_{n>=1} n|d_n|^2 ≤ 1 where d_n are coefficients of h(z)-z_j = 1/z + d0 + d1 z + d2 z^2 + ... . Here d0 = c0 - z_j, d1 = c1, d2 = c2, etc. So we get |c1| ≤ 1 (since n=1 term gives 1*|c1|^2 ≤ sum ≤ 1). So |c1| ≤ 1. That's independent of j. So we get a bound on c1, not on z1 - z2.

But maybe we need to consider the difference of the two functions h(z)-z1 and h(z)-z2. Their difference is constant (z2 - z1). Not helpful.

Alternatively, consider the product? Hmm.

Let's search memory: There is a known lemma: If p(z) = 1/z + β0 + β1 z + ... is univalent in D, then |β1| ≤ 1. That's exactly part (c) with n=1. So we have |c1| ≤ 1. Then if h omits z1 and z2, we can consider the function

φ(z) = \frac{h(z) - z1}{h(z) - z2}.

As argued, this omits 0,1,∞, thus constant. But wait, we need to check that φ is holomorphic on D. h is meromorphic with a simple pole at 0; h - z1 and h - z2 also have simple poles at 0. Their ratio is holomorphic at 0 as we saw. It may have zeros or poles where numerator or denominator zero, but those correspond to h = z1 or h = z2, which are omitted, so no zeros or poles. So φ is holomorphic and nonzero on D. Moreover, φ(0) = 1 (since both numerator and denominator have same leading term 1/z). So φ is a holomorphic function on D omitting 0 and 1 (since it never equals 0 or 1). Actually does it ever equal ∞? No, because denominator never zero. So it omits 0,1,∞. By Picard, φ is constant. Since φ(0)=1, φ ≡ 1. Therefore h(z)-z1 ≡ h(z)-z2 => z1 = z2. So the only way h can omit two values is if they are equal. Thus the hypothesis that h omits two distinct values cannot happen unless h is constant? But h is not constant because of pole. So the lemma is vacuously true: If h omits two values, then they must be equal, so |z1 - z2| = 0 ≤ 4. But the lemma likely expects a nontrivial bound for the case where h omits two values (maybe allowing h to be meromorphic with a pole at 0 but not necessarily injective? Actually they said injective). The Picard argument shows that any meromorphic function on D omitting three values is constant. Here we have a meromorphic function h with a simple pole at 0; if it omits two values, then the function (h - z1)/(h - z2) omits 0,1,∞, thus constant, leading to z1=z2. So indeed a non-constant meromorphic function on D cannot omit two distinct values. So the lemma is true but trivial: the hypothesis forces z1=z2, so the conclusion holds. However, the problem likely expects a nontrivial proof using area theorem, not Picard. Perhaps they want to avoid using Picard and instead use area theorem to get a quantitative bound that yields the constant 4, which is sharp (the Koebe function omits -1/4 only one value, but if we consider two omitted values, the maximum distance is 4, attained when the omitted values are 2 and -2? Actually consider the function h(z) = 1/z + c0. This omits infinity? Not sure. Let's test: h(z) = 1/z + c0. This is injective? For nonzero c0, it's a Möbius transformation: h(z) = (1 + c0 z)/z. This is injective on D\{0}? It's a linear fractional transformation, injective on its domain (the Riemann sphere). It omits the value c0? Actually solve h(z) = w => (1 + c0 z)/z = w => 1 + c0 z = w z => 1 = (w - c0) z => z = 1/(w - c0). This has a solution in D if |1/(w - c0)| < 1 => |w - c0| > 1. So h omits the disk of radius 1 centered at c0? Actually the image is {w: |w - c0| > 1} ∪ {∞}? Wait as z→0, h(z)→∞; as z→∞? Not relevant. So h omits the closed disk of radius 1 around c0? Actually the equation gives a unique z for each w ≠ c0; that z lies in D iff |w - c0| > 1. So the image of D\{0} under h is {w: |w - c0| > 1} ∪ {∞}. So h omits the open disk of radius 1 around c0. So it omits infinitely many values, not just two. So the hypothesis of omitting two values is very weak; many functions omit many values. So the lemma must be nontrivial: If a univalent function (with pole at 0) omits two specific values, then those values cannot be too far apart. For example, the function h(z) = 1/z omits 0 and ∞? Actually h(z)=1/z omits 0? No, h(z)=1/z takes all nonzero values; it omits 0 and ∞? As z→0, h→∞, so ∞ is attained as a limit but not as a value? In meromorphic functions, ∞ is allowed as a value at poles. So h(z)=1/z has a pole at 0, so it attains ∞ at z=0. So it omits 0 only. So it omits one value. To omit two values, we need something like h(z) = 1/z + c, which omits a disk of radius 1 around c, thus omits infinitely many values. So the hypothesis is satisfied for many functions. The lemma then gives a bound on the distance between any two omitted values: they must lie within distance 4 of each other. For h(z)=1/z + c, the omitted set is the disk |w - c| ≤ 1. Any two points in that disk have distance at most 2. So the bound 4 is not sharp for this example; but there may be functions where the omitted set is exactly two points? Actually can a univalent function omit exactly two values? Possibly yes, e.g., a covering map of the sphere minus two points? But on the disk, maybe not. The extremal case for the lemma likely gives distance 4, achieved by some function that omits two values exactly at distance 4, like the function h(z) = 1/z + 2/z^2? Not sure.

Nevertheless, we need to produce a proof using area theorem as hinted. Let's try to derive bound on |z1 - z2| from the coefficients.

We have h(z) = 1/z + c0 + c1 z + c2 z^2 + ... injective.

Define A_j(z) = 1/(h(z) - z_j). As computed, A_j(z) = z - (c0 - z_j) z^2 + O(z^3). So A_j(z)/z = 1 - (c0 - z_j) z + O(z^2). So log(A_j(z)/z) is holomorphic near 0.

Alternatively, consider the function B_j(z) = 1/A_j(z) = h(z) - z_j = 1/z + (c0 - z_j) + c1 z + ... . This is of the form required in part (c). So we have sum_{n>=1} n|d_n^{(j)}|^2 ≤ 1 where d_n^{(j)} are coefficients of B_j(z). In particular, |c1| ≤ 1 (since d_1^{(j)} = c1). So we get |c1| ≤ 1.

Now consider the difference B_1(z) - B_2(z) = (h(z)-z1) - (h(z)-z2) = z2 - z1, a constant. So the difference of the two functions is constant. Write B_j(z) = 1/z + β0^{(j)} + β1 z + β2 z^2 + ... where β0^{(j)} = c0 - z_j, β1 = c1, β2 = c2, etc. So B_1(z) - B_2(z) = (β0^{(1)} - β0^{(2)}) = (c0 - z1) - (c0 - z2) = z2 - z1. So the constant difference is z2 - z1.

Now we can apply part (c) to each B_j to get bounds on their coefficients. In particular, we have |β1| = |c1| ≤ 1. Also we have sum_{n>=1} n|β_n^{(j)}|^2 ≤ 1.

Now consider the function C(z) = B_1(z) + B_2(z). Its expansion: C(z) = 2/z + 2c0 - (z1+z2) + 2c1 z + 2c2 z^2 + ... . Not sure.

Maybe we can consider the function D(z) = B_1(z) * B_2(z). Its expansion will involve terms like 1/z^2 etc. Then apply area theorem to something like sqrt(D)? Not sure.

Alternatively, consider the function E(z) = 1/(B_1(z) B_2(z)). Since B_j(z) = h(z)-z_j, and h omits z1 and z2, we have B_j(z) ≠ 0. So E(z) is holomorphic on D. Moreover, as z→0, B_j(z) ~ 1/z, so E(z) ~ z^2. So E has a zero of order 2 at 0. Then we can consider F(z) = sqrt(E(z))? Choose a branch of sqrt such that F(z) ~ z near 0. Then F(z) is holomorphic, injective? Not sure.

But the hint says: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j). That is A_j(z). So they want to examine the coefficient of z^2 in A_j(z), which is -(c0 - z_j). Then maybe apply part (c) to something like 1/A_j(z) - 1/z? Let's see.

We have A_j(z) = z - (c0 - z_j) z^2 + O(z^3). So define C_j(z) = A_j(z)/z = 1 - (c0 - z_j) z + O(z^2). Then C_j(z) is holomorphic and nonzero at 0 (value 1). Then consider D_j(z) = 1/C_j(z) = z/A_j(z) = h(z)-z_j = 1/z + (c0 - z_j) + c1 z + ... . So we are back.

Maybe we can apply part (c) to the function (A_j(z))/z? That is C_j(z). But C_j(z) is holomorphic and nonzero at 0, not of the form 1/z + ... . However we could consider its reciprocal, which is B_j(z). So we already did.

Thus the hint might be misinterpreted: The "second coefficient" might refer to the coefficient of z in the expansion of 1/(h(z)-z_j) after factoring out the leading term 1/z? Let's check: If we write 1/(h(z)-z_j) = (1/z) * something? Actually we earlier wrote h(z)-z_j = (1/z)*(1 + (c0 - z_j)z + c1 z^2 + ...). Then its reciprocal is z * (1 + (c0 - z_j)z + c1 z^2 + ...)^{-1} = z - (c0 - z_j) z^2 + ... . So the expansion of 1/(h(z)-z_j) starts with z term. So the "second coefficient" could be the coefficient of z^2, which is -(c0 - z_j). Then we can apply part (c) to the function (1/(h(z)-z_j))/z? That gives 1 - (c0 - z_j)z + ... . Its derivative at 0 is -(c0 - z_j). Not sure.

Alternatively, maybe they want to apply part (c) to the function (1/(h(z)-z_j))'? Let's compute derivative: d/dz [1/(h(z)-z_j)] = -h'(z)/(h(z)-z_j)^2. Not helpful.

Let's step back and think about the known proof of Koebe 1/4 theorem using the area theorem. The standard proof goes: Suppose f is univalent, f(0)=0, f'(0)=1, and f omits w ≠ 0. Define F(z) = z f'(z)/(f(z)-w). Show that F is univalent in D, F(0)=1, and F omits 0. Then apply the area theorem to F' or something to get |w| ≥ 1/4. Actually there is a known lemma: If p(z) = 1 + p1 z + p2 z^2 + ... is univalent in D and has positive real part, then |p1| ≤ 2. That's related.

But the problem's structure: (c) proves area theorem bound for functions with simple pole at 0. (d) constructs g such that g^2(z)=f(z^2). (e) uses that to bound a2. (f) uses the bound on a2 to get a bound on omitted values distance. (g) completes the proof.

Thus (f) likely uses the result from (e) that |a2| ≤ 2 for normalized univalent functions. Then they consider some transformation to get a bound on omitted values.

Let's try to reconstruct: Suppose h(z) = 1/z + c0 + c1 z + ... is injective on D and omits z1 and z2. Consider the function

H(z) = \frac{1}{h(z) - z1} - \frac{1}{h(z) - z2}.

As we computed, H(z) = (z2 - z1) + higher order terms? Actually we computed H(z) = (a - b) z^2 + ...? Wait we computed difference of reciprocals gave (a - b) z^2 + ... . Let's recompute carefully:

Let A(z) = 1/(h(z)-z1), B(z) = 1/(h(z)-z2). Then

A(z) = z - (c0 - z1) z^2 + O(z^3)
B(z) = z - (c0 - z2) z^2 + O(z^3)

Thus A(z) - B(z) = [-(c0 - z1) + (c0 - z2)] z^2 + O(z^3) = (z1 - z2) z^2 + O(z^3). So

A(z) - B(z) = (z1 - z2) z^2 + O(z^3).

Thus (A(z) - B(z))/z^2 = (z1 - z2) + O(z). So the function

Φ(z) = (A(z) - B(z))/z^2

is holomorphic on D (since numerator has zero of order at least 2 at 0) and Φ(0) = z1 - z2.

Now, can we relate Φ to something like derivative of a univalent function? Note that A(z) = 1/(h(z)-z1) and B(z) = 1/(h(z)-z2). Both A and B are holomorphic on D (since h omits z1,z2). Moreover, they are injective? Not necessarily.

But maybe we can consider the function

Ψ(z) = \frac{A(z)}{B(z)} = \frac{h(z)-z2}{h(z)-z1}.

This omits 0, ∞, and 1? Actually as before, it omits 0 and ∞ because numerator and denominator never zero. It also omits 1 because that would imply z1=z2. So Ψ omits three values, thus constant by Picard, leading to z1=z2. So again trivial.

Thus the area theorem approach must avoid Picard and give a quantitative bound.

Let's search memory: There is a known result: If p(z) = 1 + p1 z + p2 z^2 + ... is univalent in D and has positive real part, then |p1| ≤ 2. This is proved via area theorem applied to something like z p'(z)/p(z). The Koebe 1/4 theorem can be derived from this: If f omits w, then the function p(z) = (w + f(z))/(w - f(z)) has positive real part and is univalent, etc.

But the problem's (f) is likely a step towards that: If h omits z1 and z2, then consider the function

φ(z) = \frac{h(z) - z1}{h(z) - z2}.

This maps D into C \ {0,1,∞}. By Picard, it's constant, but we want to avoid Picard and instead use area theorem to get a bound on the distance between z1 and z2. Perhaps we can consider the logarithm of φ, which is holomorphic (since φ omits 0 and ∞) and then bound its derivative at 0 using area theorem applied to something like exp? Not sure.

Alternatively, consider the function

χ(z) = \frac{1}{h(z) - z1} + \frac{1}{h(z) - z2}.

Its expansion: χ(z) = 2z - (2c0 - z1 - z2) z^2 + O(z^3). So χ(z)/z = 2 - (2c0 - z1 - z2) z + O(z^2). So the function

ψ(z) = χ(z)/z

is holomorphic, ψ(0)=2. Moreover, ψ omits something? Since h omits z1 and z2, the denominators never zero, so χ is holomorphic and never zero? Actually χ could be zero? Possibly. But maybe we can consider 1/ψ(z) and apply area theorem.

Let's compute 1/ψ(z) = z/χ(z). As z→0, χ(z) ~ 2z, so 1/ψ(z) ~ z/(2z) = 1/2. So 1/ψ is holomorphic at 0 with value 1/2. Not helpful.

Maybe we should consider the function

η(z) = \frac{h(z) - z1}{h(z) - z2} - 1 = \frac{z2 - z1}{h(z) - z2}.

This is holomorphic (since denominator never zero) and omits 0? Actually η(z) = 0 iff numerator zero => z2=z1, which we assume distinct, so η never zero. Also η(z) = ∞? No, denominator never zero. So η omits 0 and ∞. So 1/η is holomorphic and omits 0 and ∞? Actually 1/η = (h(z)-z2)/(z2 - z1). This is just a scaled version of h(z)-z2, which omits 0? Wait h(z)-z2 omits 0 because h omits z2. So 1/η omits 0 as well. So 1/η omits 0 and ∞? Actually 1/η is holomorphic and never zero (since h(z)-z2 never zero). It may have poles? No, it's holomorphic. So 1/η omits 0 and ∞? It never takes 0, and as a holomorphic function on D, it cannot have an essential singularity at boundary? But it's holomorphic, so it never equals ∞ (since ∞ is not a value in C). So 1/η omits 0 only. Not helpful.

Let's step back and think about the area theorem proof for the bound on omitted values. Suppose f is univalent, f(0)=0, f'(0)=1, and f omits w. Consider the function

F(z) = \frac{z f'(z)}{f(z) - w}.

One can show that F is univalent in D, F(0)=1, and F omits 0. Then apply the area theorem to F' or to something like (F(z)-1)/z to get a bound on w.

Actually, there is a known proof: If f omits w, then the function

g(z) = \frac{f(z)}{w - f(z)}

is univalent, g(0)=0, g'(0) = -1/w, and g omits 0. Then normalize to get a function with derivative 1 at 0, apply the bound on a2 to get |w| ≥ 1/4.

Let's try: Suppose f omits w ≠ 0. Define

g(z) = \frac{w f(z)}{w - f(z)}.

Then g(0)=0. Compute g'(0): g(z) = w f(z) * (w - f(z))^{-1}. At 0, f(z)=z+..., so w - f(z) = w - z - ... . Expand (w - f(z))^{-1} = w^{-1} (1 - f(z)/w)^{-1} = w^{-1} (1 + f(z)/w + ...). So g(z) = w f(z) * w^{-1} (1 + f(z)/w + ...) = f(z) (1 + f(z)/w + ...) = f(z) + f(z)^2/w + ... . Since f(z)=z+..., we get g(z) = z + (1/w + a2) z^2 + ...? Let's compute precisely: f(z) = z + a2 z^2 + a3 z^3 + ... . Then f(z)^2 = z^2 + 2 a2 z^3 + ... . So g(z) = f(z) + f(z)^2/w + ... = (z + a2 z^2 + ...) + (1/w)(z^2 + 2 a2 z^3 + ...) + ... = z + (a2 + 1/w) z^2 + ... . So g'(0)=1, g(z) = z + b2 z^2 + ... with b2 = a2 + 1/w.

Now g is univalent? Need to check: The map z -> w f(z)/(w - f(z)) is a composition of f with a Möbius transformation that maps the omitted value w to ∞ and 0 to 0. Since f is univalent and omits w, the Möbius transformation is injective on the image of f, so g is univalent. Also g(0)=0, g'(0)=w f'(0)/(w - f(0))^2? Actually derivative formula: g(z) = w f(z)/(w - f(z)). Differentiate: g' = [w f'(z)(w - f(z)) + w f(z) f'(z)]/(w - f(z))^2 = w w f'(z)/(w - f(z))^2? Let's compute: numerator: w f'(z)(w - f(z)) + w f(z) f'(z) = w f'(z)[w - f(z) + f(z)] = w f'(z) w = w^2 f'(z). Denominator: (w - f(z))^2. So g'(z) = w^2 f'(z)/(w - f(z))^2. At z=0, f(0)=0, f'(0)=1, so g'(0) = w^2 * 1 / w^2 = 1. Good.

Thus g is a normalized univalent function (holomorphic, injective, g(0)=0, g'(0)=1). Moreover, g omits 0? Check: g(z)=0 iff numerator w f(z)=0 => f(z)=0 => z=0 (since f injective and f(0)=0). So g(z)=0 only at z=0, but 0 is in the domain; however we consider omitted values in the image of g on D\{0}? Actually g(0)=0, so 0 is attained. But we want g to omit 0? Wait we want to apply the bound on a2 to g, which requires g to be univalent and normalized. It does not need to omit anything. So we can directly apply part (e) to g to get |b2| ≤ 2. That gives |a2 + 1/w| ≤ 2. Since we also have from part (e) that |a2| ≤ 2 for f, we can combine to get a bound on w. Indeed, triangle inequality: |1/w| = |b2 - a2| ≤ |b2| + |a2| ≤ 2 + 2 = 4, so |w| ≥ 1/4. This yields Koebe 1/4 theorem.

Thus part (f) might be a lemma that if h omits z1 and z2, then |z1 - z2| ≤ 4, which is analogous to the bound we just derived: For g above, we had |b2| ≤ 2 and |a2| ≤ 2, leading to |1/w| ≤ 4. In that context, z1 and z2 correspond to 0 and 1/w? Let's see: In the proof, we considered f omits w. Then we looked at 1/f omits 0 and 1/w. So h = 1/f has the form 1/z + ... and omits 0 and 1/w. Then applying (f) to h with z1=0, z2=1/w gives |1/w - 0| ≤ 4 => |w| ≥ 1/4. So indeed (f) is exactly the statement: If h(z) = 1/z + c0 + c1 z + ... is injective on D and omits two values z1 and z2, then |z1 - z2| ≤ 4.

Thus we need to prove (f) using the bound on a2 from (e). How can we get that? Let's try to derive (f) from (e). Suppose h(z) = 1/z + c0 + c1 z + ... is injective on D and omits z1 and z2. Consider the function

H(z) = \frac{1}{h(z) - z1} - \frac{1}{h(z) - z2}.

As we computed, H(z) = (z1 - z2) z^2 + O(z^3). So H(z)/z^2 = (z1 - z2) + O(z). So the function

φ(z) = \frac{H(z)}{z^2}

is holomorphic on D, φ(0) = z1 - z2.

Now, can we relate φ to something like derivative of a univalent function? Note that

H(z) = \frac{1}{h(z)-z1} - \frac{1}{h(z)-z2} = \frac{(h(z)-z2) - (h(z)-z1)}{(h(z)-z1)(h(z)-z2)} = \frac{z1 - z2}{(h(z)-z1)(h(z)-z2)}.

Thus

φ(z) = \frac{z1 - z2}{z^2 (h(z)-z1)(h(z)-z2)}.

So

\frac{1}{φ(z)} = \frac{z^2 (h(z)-z1)(h(z)-z2)}{z1 - z2}.

Now, consider the function

ψ(z) = z \sqrt{ \frac{(h(z)-z1)(h(z)-z2)}{z1 - z2} } ?

Not sure.

Alternatively, consider the function

F(z) = \frac{z}{h(z)-z1} + \frac{z}{h(z)-z2}.

Its expansion: F(z) = 2 - (2c0 - z1 - z2) z + O(z^2). So F(z) is holomorphic, F(0)=2. Moreover, maybe we can show that F is univalent? Not sure.

Let's think about using the bound on a2 from (e). For a normalized univalent function f(z)=z + a2 z^2 + ..., we have |a2| ≤ 2. How can we relate h to such an f? Since h has a pole at 0, we can consider f(z) = 1/h(z). Then f(0)=0? Let's check: h(z) = 1/z + c0 + c1 z + ... => near 0, h(z) ~ 1/z, so 1/h(z) ~ z. So f(z) = 1/h(z) is holomorphic at 0 with f(0)=0. Moreover, f'(0) = ? Compute: f(z) = 1/h(z) = z / (1 + c0 z + c1 z^2 + ...). Expand: f(z) = z (1 - c0 z + (c0^2 - c1) z^2 + ... ) = z - c0 z^2 + (c0^2 - c1) z^3 + ... . So f'(0)=1. Also f is injective? Since h is injective and nonzero? Actually h is injective and never zero? Does h omit 0? Not necessarily; h may take 0. But if h is injective and has a pole at 0, then h(z)=0 may have at most one solution. However, f(z)=1/h(z) will be injective if h is injective and never zero? Let's check: Suppose f(z1)=f(z2). Then 1/h(z1)=1/h(z2) => h(z1)=h(z2) => z1=z2 by injectivity of h. So f is injective wherever h(z1) and h(z2) are finite and nonzero. However, if h(z)=0 at some point, then f has a pole there? Actually if h(z0)=0, then f(z0) is infinite (pole). But f is supposed to be holomorphic on D? We defined f(z)=1/h(z). Since h is meromorphic with a simple pole at 0, h may have zeros elsewhere. Then f will have poles at those zeros, so f may not be holomorphic on all D. However, we can possibly restrict to a smaller disk where h has no zeros? Not guaranteed.

But maybe we can choose a rotation or translation to ensure h omits 0? In the application to Koebe theorem, h=1/f omits 0 because f(0)=0 and f injective => f(z)≠0 for z≠0, so 1/f omits 0. So in that case, h omits 0. So in (f), we might be able to assume that one of the omitted values is 0? Actually the statement of (f) is general: h omits z1 and z2. But we can apply it to h=1/f which omits 0 and 1/w. So one omitted value is 0. So perhaps we can prove (f) under the assumption that one of the omitted values is 0, and then the general case follows by translation? Let's see: If h omits z1 and z2, then consider H(z) = h(z) - z1. Then H omits 0 and z2 - z1. Moreover, H(z) = 1/z + (c0 - z1) + c1 z + ... . So H is of the same form (simple pole at 0 with residue 1) and omits 0 and some value W = z2 - z1. Then we want to show |W| ≤ 4. So it suffices to prove the lemma under the assumption that one omitted value is 0. Then the general case follows by subtracting z1.

Thus we can assume w.l.o.g. that h omits 0 and some value W. Then we want to show |W| ≤ 4.

Now, h omits 0 means h(z) ≠ 0 for all z in D. Since h has a simple pole at 0 with residue 1, near 0 h(z) ≈ 1/z, so it's large, not zero. So omitting 0 is plausible.

Now, define f(z) = 1/h(z). Then f is holomorphic on D? Since h omits 0, h(z) never zero, so f(z) = 1/h(z) is holomorphic on D. Moreover, f(0) = 0 because h(z) ~ 1/z => f(z) ~ z. Compute f'(0) = 1 as before. Also f is injective? Since h is injective and never zero, f(z1)=f(z2) => 1/h(z1)=1/h(z2) => h(z1)=h(z2) => z1=z2. So f is injective. Moreover, f omits the value 1/W? Because h omits W => 1/h omits 1/W? Actually if h(z) ≠ W for all z, then f(z) = 1/h(z) ≠ 1/W. So f omits 1/W. Also f(0)=0, f'(0)=1. So f is a normalized univalent function omitting the value 1/W. Then by part (e) we have |a2| ≤ 2 for f. But we also can compute a2 in terms of h's coefficients. Let's compute.

Given h(z) = 1/z + c0 + c1 z + c2 z^2 + ... . Since h omits 0, we can write f(z) = 1/h(z). Expand:

Let h(z) = (1/z) * H(z) where H(z) = 1 + c0 z + c1 z^2 + c2 z^3 + ... . Then f(z) = z / H(z) = z * (1 - c0 z + (c0^2 - c1) z^2 + (-c0^3 + 2c0 c1 - c2) z^3 + ... ). So

f(z) = z - c0 z^2 + (c0^2 - c1) z^3 + ... .

Thus f(z) = z + a2 z^2 + a3 z^3 + ... with a2 = -c0.

Wait check: coefficient of z^2 is -c0. So a2 = -c0.

Now, f omits the value 1/W. So we can apply the bound on a2 from part (e) to f? Part (e) gave |a2| ≤ 2 for any normalized univalent function. So we get |c0| ≤ 2.

But we need a bound on W, not on c0. How to get W from c0 and maybe c1? Let's also compute the coefficient a3 maybe related to W.

Alternatively, we can consider the function g(z) = 1/(f(z) - 1/W). Since f omits 1/W, this function is holomorphic, etc. Might lead to bound.

But perhaps there is a more direct way: Use the area theorem on the function

Φ(z) = \frac{1}{h(z)} + \frac{1}{h(z) - W}.

Since h omits 0 and W, both denominators never zero. Let's compute its expansion.

We have 1/h(z) = f(z) = z - c0 z^2 + ... .

Also 1/(h(z)-W) = ? Let's compute: h(z)-W = 1/z + (c0 - W) + c1 z + ... . Its reciprocal: we can compute similarly: 1/(h(z)-W) = z - (c0 - W) z^2 + ... .

Thus

Φ(z) = (z - c0 z^2 + ...) + (z - (c0 - W) z^2 + ...) = 2z - (2c0 - W) z^2 + ... .

So Φ(z)/z = 2 - (2c0 - W) z + ... .

Now, consider the function Ψ(z) = Φ(z)/z. It is holomorphic, Ψ(0)=2. Moreover, maybe we can show that Ψ is univalent? Not sure.

Alternatively, consider the function

Ω(z) = \frac{Φ(z)}{2} = z - \frac{2c0 - W}{2} z^2 + ... .

This is of the form z + A z^2 + ... with A = -(2c0 - W)/2. If we could show that Ω is univalent, then by part (e) we would have |A| ≤ 2, giving |2c0 - W| ≤ 4. Combined with |c0| ≤ 2 from earlier, we could bound |W| ≤ |2c0| + |2c0 - W| ≤ 4 + 4 = 8, not good.

But maybe we can show that Ω is univalent without extra assumptions? Let's test: Ω(z) = (1/(2h(z)) + 1/(2(h(z)-W))). Not obviously univalent.

Let's step back and think about the known proof of the lemma using area theorem directly on h. Perhaps we can apply area theorem to the function

H(z) = \frac{1}{h(z)} + \frac{1}{h(z) - W}.

We computed its expansion: H(z) = 2z - (2c0 - W) z^2 + ... . So H(z) has a simple zero at 0? Actually leading term 2z, so zero of order 1. Then consider K(z) = H(z)/z = 2 - (2c0 - W) z + ... . This is holomorphic and nonzero at 0 (value 2). Then consider L(z) = 1/K(z) = z/H(z). This has expansion: L(z) = (1/2) z + ...? Actually compute: H(z) = 2z + α z^2 + ... where α = -(2c0 - W). Then 1/H(z) = (1/(2z)) * 1/(1 + (α/(2)) z + ...) = (1/(2z)) (1 - (α/2) z + ...) = 1/(2z) - α/4 + ... . So L(z) = z/H(z) = 1/2 - (α/4) z + ... . So L(z) is holomorphic at 0 with value 1/2. Not helpful.

Maybe we should consider the function

M(z) = \frac{h(z)}{h(z) - W}.

Since h omits 0 and W, this is holomorphic and never 0 or ∞? Actually numerator never zero (h omits 0), denominator never zero (h omits W). So M is holomorphic and nonzero. Moreover, as z→0, h(z) ~ 1/z, so M(z) ~ (1/z)/(1/z) = 1. So M(0)=1. Also M omits 1? Because M(z)=1 would imply h(z) = h(z)-W => W=0, which is false if W≠0. So M omits 0,1,∞. Thus by Picard, M is constant, leading to W=0. So again Picard gives triviality. So we need to avoid Picard.

Thus the area theorem approach must give a bound without invoking Picard, and the bound 4 is not sharp for the case where one omitted value is 0? Actually if h omits 0 and W, then the function M(z) = h(z)/(h(z)-W) omits 0,1,∞, so by Picard it's constant, forcing W=0. So any non-constant h cannot omit both 0 and another value? Wait that would imply that a meromorphic function on D with a simple pole at 0 cannot omit two values, one of which is 0. But we have examples: h(z) = 1/z + c omits a disk of radius 1 around c, which includes 0 if |c| < 1? Actually if c=0, h(z)=1/z omits 0? No, h(z)=1/z takes all nonzero values, omits 0? As z→0, h→∞, but 0 is not attained because equation 1/z = 0 has no solution. So h(z)=1/z omits 0. Does it omit another value? It omits no other finite value because for any w ≠ 0, solve 1/z = w => z = 1/w, which is in D if |1/w| < 1 => |w| > 1. So h omits the closed disk |w| ≤ 1? Actually for |w| ≤ 1, the solution z = 1/w has |z| ≥ 1, so not in D (except maybe boundary). So h(z)=1/z omits the closed unit disk. So it omits infinitely many values, including 0 and many others. So h omits 0 and also omits, say, 0.5. So h omits two values (0 and 0.5). Yet h is not constant. So the Picard argument fails because M(z) = h(z)/(h(z)-0.5) is not holomorphic? Let's check: h(z) = 1/z. Then M(z) = (1/z) / (1/z - 0.5) = 1 / (1 - 0.5 z). This is holomorphic on D (since denominator 1 - 0.5 z ≠ 0 for |z|<2). It omits 0? Numerator 1, never zero. It omits ∞? Denominator never zero. It omits 1? Solve 1/(1-0.5z)=1 => 1 = 1 - 0.5z => z=0. So at z=0, M(0)=1. So M takes the value 1 at z=0. So M does not omit 1; it attains 1 at 0. So the earlier claim that M omits 1 is false: M(z)=1 iff h(z) = h(z)-W => W=0, but we forgot that h(z) may be infinite? Actually solving M(z)=1 gives h(z)/(h(z)-W)=1 => h(z) = h(z)-W => W=0. So if W≠0, the equation has no solution in C where h(z) is finite. However, if h(z) has a pole, then both numerator and denominator are infinite, and the ratio may be defined as limit. At a pole of h, both numerator and denominator have a pole; the ratio may tend to 1. Indeed, at z=0, h has a pole, so we need to evaluate limit: lim_{z→0} h(z)/(h(z)-W) = lim (1/z + ...)/(1/z + ... - W) = 1. So M(z) can equal 1 at the pole (by continuous extension). So M omits 0 and ∞, but may attain 1. So M omits only two values (0 and ∞), not three. So Picard's theorem for holomorphic functions (which requires omitting three values) does not apply because M is holomorphic and omits only 0 and ∞ (i.e., never 0 and never ∞). Actually omitting ∞ means it's bounded? No, a holomorphic function on D can omit ∞ trivially because ∞ is not a value in C; the condition of omitting ∞ is vacuous for holomorphic functions. So Picard's little theorem says a holomorphic function from D to C omitting two values is constant. Here M omits 0 only? Wait M never equals 0 because numerator never zero. Does M ever equal ∞? No, as a holomorphic function, it never equals ∞. So M omits 0 and ∞? But omitting ∞ is not a restriction because the codomain is C; ∞ is not in C. So the condition is just that M never takes the value 0. So M omits only one value (0). Thus Picard does not force constancy. So the earlier attempt to use Picard incorrectly assumed that omitting ∞ is a condition, but it's not for holomorphic functions. So we need a different approach.

Thus we need to prove (f) using area theorem, likely by considering the function

φ(z) = \frac{1}{h(z)} + \frac{1}{h(z) - W}

and applying part (c) to something like its reciprocal or derivative.

Let's try to derive a bound on W from the coefficients we have.

We have h(z) = 1/z + c0 + c1 z + c2 z^2 + ... . Since h omits 0 and W, we know that h(z) ≠ 0 and h(z) ≠ W for all z.

Define

A(z) = \frac{1}{h(z)} = f(z) (as before). Then f is holomorphic, f(0)=0, f'(0)=1, f omits 1/W.

Define

B(z) = \frac{1}{h(z) - W}. Then B is holomorphic, B(0)=0? Let's check: As z→0, h(z) ~ 1/z, so h(z)-W ~ 1/z, so B(z) ~ z. So B(0)=0. Also B'(0)=1? Compute: B(z) = 1/(h(z)-W) = z / (1 + (c0 - W)z + c1 z^2 + ...). Expand: B(z) = z (1 - (c0 - W)z + ...) = z - (c0 - W) z^2 + ... . So B'(0)=1. Also B is injective? Since h is injective and omits W, h(z1)-W = h(z2)-W => h(z1)=h(z2) => z1=z2. So B is injective. Moreover, B omits the value -W/(??) Actually B omits? Since h omits W, B never has pole? Actually B is holomorphic; does B omit any value? B(z) = 0 only if h(z)-W has a pole, i.e., h(z) has a pole, which only occurs at z=0. At z=0, B(0)=0. So B attains 0 only at z=0. So B omits no nonzero value? Not sure.

But we have two normalized univalent functions f and B, both with f(0)=B(0)=0, f'(0)=B'(0)=1. Their coefficients: f(z) = z - c0 z^2 + (c0^2 - c1) z^3 + ... ; B(z) = z - (c0 - W) z^2 + ... .

Thus the coefficient of z^2 in f is a2 = -c0; in B is b2 = -(c0 - W) = -c0 + W.

Now, by part (e), we know that for any normalized univalent function, |a2| ≤ 2 and |b2| ≤ 2. So we have

|c0| ≤ 2,
| -c0 + W | ≤ 2.

Thus |W| = |(-c0 + W) + c0| ≤ | -c0 + W| + |c0| ≤ 2 + 2 = 4.

Thus |W| ≤ 4. This proves (f) under the assumption that h omits 0 and W. Then the general case follows by translation: if h omits z1 and z2, then H(z) = h(z) - z1 omits 0 and W = z2 - z1, and H is of the same form (simple pole at 0 with residue 1). Applying the above yields |z2 - z1| ≤ 4.

Thus (f) is proved using (e) and the construction of f and B as reciprocals of h and h-W. This matches the hint: "Look at the second coefficient in the power series expansion of 1/(h(z) - z_j)." Indeed, 1/(h(z)-z_j) is B_j(z) (up to maybe a factor). Its expansion gives the coefficient of z^2 as -(c0 - z_j). Then applying part (e) to the function 1/(h(z)-z_j) (which is normalized univalent) yields bound on that coefficient, leading to bound on difference.

Thus we have a clear path for (f). Let's flesh out details:

- Show that if h omits z1 and z2, then for each j, the function f_j(z) = 1/(h(z)-z_j) is holomorphic on D, satisfies f_j(0)=0, f_j'(0)=1, and is injective (since h is injective and omits z_j). Then apply part (e) to f_j to get |a_{2}^{(j)}| ≤ 2, where a_{2}^{(j)} is the coefficient of z^2 in f_j's expansion.

- Compute the expansion: f_j(z) = z - (c0 - z_j) z^2 + O(z^3). So a_{2}^{(j)} = -(c0 - z_j).

- Hence |c0 - z_j| ≤ 2 for j=1,2.

- Then by triangle inequality, |z1 - z2| = |(c0 - z2) - (c0 - z1)| ≤ |c0 - z2| + |c0 - z1| ≤ 2 + 2 = 4.

Thus (f) proved.

Now we need to ensure that f_j is indeed injective: h is injective and omits z_j, so h(z1)-z_j = h(z2)-z_j implies h(z1)=h(z2) implies z1=z2. So f_j is injective.

Also need to check that f_j is holomorphic on D: Since h omits z_j, denominator never zero, so f_j is holomorphic. At z=0, h has a pole, so h(z)-z_j also has a pole, but its reciprocal has a removable zero? Actually as we computed, f_j(z) = z * (something holomorphic and nonzero at 0), so f_j is holomorphic at 0 with f_j(0)=0.

Now we need to verify f_j'(0)=1. Compute derivative: f_j(z) = 1/(h(z)-z_j). Write h(z) = 1/z + φ(z) where φ(z) = c0 + c1 z + c2 z^2 + ... . Then h(z)-z_j = 1/z + (c0 - z_j) + φ(z) - c0? Actually φ(z) already includes c0, so h(z)-z_j = 1/z + (c0 - z_j) + c1 z + c2 z^2 + ... . Then f_j(z) = z / [1 + (c0 - z_j) z + c1 z^2 + c2 z^3 + ...] = z * [1 - (c0 - z_j) z + ((c0 - z_j)^2 - c1) z^2 + ...]. So f_j(z) = z - (c0 - z_j) z^2 + ... . So f_j'(0)=1.

Thus part (e) applies.

Now part (e) itself: We need to prove |a2| ≤ 2 for normalized univalent f(z)=z + a2 z^2 + ... . The solution sketch used part (d) and (c). Let's verify that proof.

Part (d): Given f normalized univalent, show there exists g normalized univalent such that g^2(z) = f(z^2). Construction: Since f(z)/z is nowhere zero and holomorphic on D, we can define a holomorphic square root ψ with ψ(0)=1. Then set g(z) = z ψ(z^2). Show g is injective, g(0)=0, g'(0)=1, and g^2(z) = f(z^2). Need to verify injectivity: Suppose g(z1)=g(z2). Then z1 ψ(z1^2) = z2 ψ(z2^2). Square both sides: z1^2 ψ(z1^2)^2 = z2^2 ψ(z2^2)^2 => f(z1^2) = f(z2^2). Since f is injective, z1^2 = z2^2. So z1 = ± z2. But g is odd? Let's check: g(-z) = (-z) ψ((-z)^2) = -z ψ(z^2) = -g(z). So g is odd. Thus if z1 = -z2, then g(z1) = -g(z2). For them to be equal, we need g(z1)=g(z2) => -g(z2)=g(z2) => g(z2)=0 => z2=0 => z1=0. So the only case is z1=z2=0. Hence injective.

Thus (d) is solid.

Part (e): Using g, we compute 1/g(z) expansion and apply (c) to get bound on a2.

Let's detail:

From (d), g(z) = z ψ(z^2) where ψ^2(z) = f(z)/z, ψ(0)=1.

Since f(z) = z + a2 z^2 + a3 z^3 + ... , we have f(z)/z = 1 + a2 z + a3 z^2 + ... . So ψ(z) = sqrt{1 + a2 z + a3 z^2 + ... } = 1 + (a2/2) z + ... . So ψ(z^2) = 1 + (a2/2) z^2 + ... . Then g(z) = z (1 + (a2/2) z^2 + ... ) = z + (a2/2) z^3 + ... . So g is odd: only odd powers.

Thus 1/g(z) = 1/z * 1/(1 + (a2/2) z^2 + ... ) = 1/z * (1 - (a2/2) z^2 + ... ) = 1/z - (a2/2) z + ... .

So 1/g(z) = 1/z + b0 + b1 z + b2 z^2 + ... with b1 = -a2/2 (coefficient of z). All other b_n for even n? Actually expansion: 1/g(z) = 1/z + b0 + b1 z + b2 z^2 + ... . Since g is odd, 1/g is odd? Let's check: g(-z) = -g(z) => 1/g(-z) = -1/g(z). So 1/g is odd as well. So its expansion contains only odd powers: 1/g(z) = 1/z + b1 z + b3 z^3 + ... . So b0 = 0, b2 = 0, etc. So b1 is the coefficient of z.

Thus by part (c) applied to 1/g(z) (which is of the form 1/z + c0 + c1 z + ... injective on punctured disc), we have sum_{n>=1} n|b_n|^2 ≤ 1. In particular, the n=1 term gives 1*|b1|^2 ≤ 1 => |b1| ≤ 1. Hence |a2/2| ≤ 1 => |a2| ≤ 2.

Equality case: If |a2|=2, then |b1|=1, and equality in the area theorem forces 1/g(z) to have the form 1/z + e^{iθ} z (i.e., only b1 nonzero). Then we can solve for g and f as in the sketch.

Thus (e) is proved.

Now (c): Prove area theorem bound.

We need to show: If h(z) = 1/z + c0 + c1 z + c2 z^2 + ... is injective on 0<|z|<1, then sum_{n>=1} n|c_n|^2 ≤ 1.

Proof: For 0<ρ<1, consider the image of the annulus? Actually we consider the image of the punctured disk D_ρ\{0} under h. Since h is injective, the area of h(D_ρ\{0}) can be computed via the Jacobian: area = ∫_{D_ρ\{0}} |h'(z)|^2 dA(z). Alternatively, we can compute the area of the complement of h(D_ρ\{0}) in the extended complex plane? The area theorem usually considers the complement of the image of a univalent function on the exterior of the unit disk. But here we have a punctured disk. However, we can apply a change of variable w = 1/z to map the punctured disk to the exterior of the unit disk. Let's do that.

Define H(w) = h(1/w). Then for |w|>1, H(w) is analytic? Let's see: h(z) = 1/z + c0 + c1 z + c2 z^2 + ... . Then h(1/w) = w + c0 + c1/w + c2/w^2 + ... . So H(w) = w + c0 + c1/w + c2/w^2 + ... for |w|>1. This is analytic on |w|>1 (the exterior of the unit disk) and has a simple pole at infinity? Actually as w→∞, H(w) ~ w + c0 + ... . So H(w) is univalent on |w|>1? Since h is injective on 0<|z|<1, the map w→1/w is a bijection between {|w|>1} and {0<|z|<1}. So H is injective on |w|>1. Moreover, H has a simple pole at w=∞? Actually as w→∞, H(w) ~ w, so it has a simple pole at infinity with residue 1. The area theorem for functions univalent on the exterior of the unit disk with expansion F(w) = w + b0 + b1/w + b2/w^2 + ... says that sum_{n>=1} n|b_n|^2 ≤ 1. This is a standard result (Gronwall's area theorem). Here our H(w) = w + c0 + c1/w + c2/w^2 + ... . So the coefficients b_n = c_n. Then the area theorem gives sum_{n>=1} n|c_n|^2 ≤ 1. This is exactly what we need.

Thus we can prove (c) by mapping to the exterior and applying the known area theorem. Or we can directly compute area of complement of h(D_ρ\{0}) and let ρ→1.

Let's produce a direct proof: For 0<ρ<1, consider the image of the circle |z|=ρ under h. Since h is injective, the curve h(|z|=ρ) is a simple closed curve. The area enclosed by this curve can be computed via Green's formula: Area = (1/2i) ∫_{|z|=ρ} \overline{h(z)} h'(z) dz. Expand h(z) and h'(z) in series, integrate term by term, get area = π(1/ρ^2 - sum_{n>=1} n|c_n|^2 ρ^{2n}). Since the area is nonnegative, we get the inequality. Then let ρ→1^- to get sum n|c_n|^2 ≤ 1.

We'll present that.

Now (a) and (b) are straightforward.

Finally (g): Complete the proof: Suppose f is normalized univalent and omits w ≠ 0. Then consider h(z) = 1/f(z). Show h is of the form 1/z + ... and omits 0 and 1/w. Apply (f) to get |1/w| ≤ 4 => |w| ≥ 1/4. Show that 1/4 is attained by the Koebe function k(z) = z/(1-z)^2, which omits -1/4. Hence the best possible radius is 1/4.

Now we need to write a full solution with proofs for each part, showing all reasoning.

Let's structure the answer:

- Introduction: restate problem.

- Part (a): Provide counterexample f_n(z)=z/n. Show f_n(0)=0, holomorphic, f_n'(0)=1/n, image is D_{1/n}(0), so 1/n not in image. Conclude no uniform r.

- Part (b): Provide f_ε(z)=ε(e^{z/ε}-1). Show f_ε(0)=0, f_ε'(0)=1, image omits -ε. Conclude no uniform r.

- Part (c): Prove area theorem bound.

   * Let h(z)=1/z + c0 + c1 z + ... be injective on 0<|z|<1.
   * For 0<ρ<1, consider the curve γ_ρ(t)=h(ρ e^{it}), t∈[0,2π]. Since h is injective, γ_ρ is a simple closed curve.
   * Compute area A(ρ) enclosed by γ_ρ using Green's theorem: A(ρ) = (1/2i) ∮_{γ_ρ} \overline{w} dw = (1/2i) ∮_{|z|=ρ} \overline{h(z)} h'(z) dz.
   * Insert series: h(z)=z^{-1}+∑_{k≥0} c_k z^k, h'(z)=-z^{-2}+∑_{k≥0} (k+1) c_{k+1} z^k.
   * Compute product and integrate termwise; only terms where powers of z cancel give nonzero contribution.
   * Obtain A(ρ)=π(ρ^{-2} - ∑_{n≥1} n|c_n|^2 ρ^{2n}).
   * Since area ≥0, we have ∑ n|c_n|^2 ρ^{2n} ≤ ρ^{-2} for all ρ<1.
   * Let ρ→1^− to get ∑ n|c_n|^2 ≤ 1.

- Part (d): Given f(z)=z + a2 z^2 + ... injective, f(0)=0, f'(0)=1.

   * Show f(z)/z is nowhere zero on D and holomorphic, with value 1 at 0.
   * Define ψ(z) a holomorphic square root of f(z)/z with ψ(0)=1 (exists because D is simply connected and f(z)/z ≠0).
   * Set g(z)=z ψ(z^2). Then g(0)=0, g'(0)=ψ(0)=1.
   * Show g^2(z)=z^2 ψ(z^2)^2 = z^2·(f(z^2)/z^2)=f(z^2).
   * Prove g is injective: Suppose g(z1)=g(z2). Then squaring gives f(z1^2)=f(z2^2) ⇒ z1^2=z2^2 ⇒ z1=±z2. If z1=-z2≠0, then g(z1)=-g(z2)≠g(z2) unless g(z2)=0 ⇒ z2=0 ⇒ z1=0. Hence z1=z2.
   * Thus g satisfies the hypotheses.

- Part (e): Bound on a2.

   * From (d), g(z)=z + (a2/2) z^3 + ... (only odd powers).
   * Hence 1/g(z)=1/z - (a2/2) z + ... .
   * Write 1/g(z)=1/z + b0 + b1 z + b2 z^2 + ... . By oddness, b0=b2=...=0, b1=-a2/2.
   * Since g satisfies the hypotheses of the theorem, 1/g is of the form 1/z + c0 + c1 z + ... injective on 0<|z|<1 (simple pole at 0, residue 1). Apply part (c): ∑ n|b_n|^2 ≤ 1 ⇒ |b1|^2 ≤ 1 ⇒ |a2|/2 ≤ 1 ⇒ |a2| ≤ 2.
   * Equality: If |a2|=2, then |b1|=1 and equality in (c) forces 1/g(z)=1/z + e^{iθ} z for some θ∈ℝ (all higher coefficients zero). Solving gives g(z)=z/(1+e^{iθ}z^2). Then f(z^2)=g(z)^2 = z^2/(1+e^{iθ}z^2)^2 ⇒ f(z)=z/(1+e^{iθ}z)^2. Conversely, these functions satisfy the hypotheses and give |a2|=2.

- Part (f): Bound on distance between two omitted values.

   * Let h(z)=1/z + c0 + c1 z + ... be injective on D and omit two distinct values z1, z2.
   * Define for j=1,2 the functions f_j(z)=1/(h(z)-z_j). Since h omits z_j, f_j is holomorphic on D. Moreover, f_j(0)=0, f_j'(0)=1, and f_j is injective (because h is injective).
   * Thus f_j satisfies the hypotheses of the theorem. By part (e), the coefficient of z^2 in f_j's expansion, call it a_2^{(j)}, satisfies |a_2^{(j)}| ≤ 2.
   * Compute the expansion: h(z)-z_j = 1/z + (c0-z_j) + c1 z + c2 z^2 + ... . Hence
        f_j(z) = 1/(h(z)-z_j) = z - (c0-z_j) z^2 + O(z^3).
     So a_2^{(j)} = -(c0-z_j).
   * Therefore |c0 - z_j| ≤ 2 for j=1,2.
   * By the triangle inequality,
        |z1 - z2| = |(c0 - z2) - (c0 - z1)| ≤ |c0 - z2| + |c0 - z1| ≤ 2 + 2 = 4.
   * Hence |z1 - z2| ≤ 4.

- Part (g): Koebe–Bieberbach radius theorem.

   * Let f be injective on D with f(0)=0, f'(0)=1. Suppose there exists w∈ℂ with |w|<1/4 such that w∉f(D). We'll derive a contradiction.
   * Since f is injective and f(0)=0, we have f(z)≠0 for z≠0. Hence the function h(z)=1/f(z) is holomorphic on D.
   * Moreover, h has a simple pole at 0 with residue 1 because f(z)=z+⋯ ⇒ h(z)=1/z+⋯. So h(z)=1/z + c0 + c1 z + ⋯.
   * Since w∉f(D), we have f(z)≠w for all z∈D. Hence h(z)≠1/w for all z∈D. Also h(z)≠0 because f(z)≠∞ (f is holomorphic) and f(z)=0 only at z=0, but h has a pole at 0, so h(z)≠0 for z≠0; at z=0, h has a pole, so we consider the punctured disk: h omits 0 on D\{0}. Thus h omits the two values 0 and 1/w on D\{0}.
   * Apply part (f) to h (which is injective on D\{0} and of the required form) to obtain |0 - 1/w| ≤ 4, i.e., |1/w| ≤ 4 ⇒ |w| ≥ 1/4.
   * This contradicts |w|<1/4. Therefore every w with |w|<1/4 belongs to f(D). Hence D_{1/4}(0) ⊆ f(D).
   * To see that 1/4 is best possible, consider the Koebe function k(z)=z/(1-z)^2. It satisfies k(0)=0, k'(0)=1, is injective on D, and its image is ℂ \ (−∞,−1/4]. In particular, −1/4∉k(D), so no larger radius works.
   * Thus the best possible constant is r=1/4.

- Conclude Q.E.D.

We need to ensure all steps are rigorous, especially the injectivity of h on D\{0} in part (g). Since f is injective on D and f(0)=0, for z1≠z2 in D\{0}, if f(z1)=f(z2) then z1=z2 by injectivity. So f is injective on D\{0} as well. Then h=1/f is also injective on D\{0} because if 1/f(z1)=1/f(z2) then f(z1)=f(z2) ⇒ z1=z2. Also h never takes the value 0 on D\{0} because f(z)≠0 for z≠0. So h omits 0 on D\{0}. Also h omits 1/w because f(z)≠w ⇒ h(z)≠1/w. So h omits two values on D\{0}. However, part (f) required h to be defined and injective on the whole D (including 0?) Actually the statement of (f) says: "If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, show that |z1 - z2| ≤ 4." It assumes h is defined on D (i.e., holomorphic on D) with that Laurent expansion (so it has a simple pole at 0). In our case, h has a simple pole at 0, so it's not holomorphic at 0 but meromorphic. However, the expansion shows it's of the form 1/z + ... . The condition "injective on D" likely means injective as a map from D to the Riemann sphere, allowing the pole at 0 to map to ∞. Usually, for such meromorphic functions, injective means that if z1≠z2 then h(z1)≠h(z2) (including the case where one or both equal ∞). Since h has a simple pole at 0, h(0)=∞. For any other z≠0, h(z) is finite, so h(z)≠∞. Thus injectivity holds if h is injective on D\{0} and h(0)=∞ is not attained elsewhere. Since f omits 0, h(z)=1/f(z) never equals 0, so h(z)≠∞? Wait h(z)=∞ only when f(z)=0, which only occurs at z=0. So h(0)=∞, and for z≠0, h(z) is finite. So h is injective on D as a map to the Riemann sphere. So the hypothesis of (f) is satisfied: h is meromorphic on D with a simple pole at 0, injective, and has the expansion 1/z + c0 + c1 z + ... . It omits the values 0 and 1/w (since h(z) never equals 0 nor 1/w). So we can apply (f) directly.

Thus part (g) works.

Now we need to write the solution in a clear, step-by-step manner, with full proofs.

Let's produce the final answer.



---

## Model Solution

**Solution**

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\).  
A function \(f:\mathbb D\to\mathbb C\) is *normalized* if \(f(0)=0\) and \(f'(0)=1\).

--------------------------------------------------------------------
### (a)  No uniform radius without further hypotheses

For \(n\in\mathbb N\) set  

\[
f_n(z)=\frac{z}{n},\qquad z\in\mathbb D .
\]

* \(f_n(0)=0\) and \(f_n\) is holomorphic on \(\mathbb D\).
* \(f_n' (z)=\frac1n\), hence \(f_n'(0)=\frac1n\).
* \(f_n(\mathbb D)=\{w:|w|<\frac1n\}=D_{1/n}(0)\); therefore \(\frac1n\notin f_n(\mathbb D)\).

If a number \(r>0\) worked for every such \(f\), then for any \(n\) we would have  
\(D_r(0)\subset f_n(\mathbb D)\).  Choosing \(n\) with \(\frac1n<r\) gives  
\(\frac1n\in D_r(0)\) but \(\frac1n\notin f_n(\mathbb D)\), a contradiction.  
Hence no such \(r\) exists.

--------------------------------------------------------------------
### (b)  The hypothesis \(f'(0)=1\) still does not give a uniform radius

For \(\varepsilon>0\) define  

\[
f_\varepsilon(z)=\varepsilon\bigl(e^{z/\varepsilon}-1\bigr),\qquad z\in\mathbb D .
\]

* \(f_\varepsilon(0)=0\) and  
  \(f_\varepsilon'(z)=e^{z/\varepsilon}\), so \(f_\varepsilon'(0)=1\).
* Since \(e^{z/\varepsilon}\neq0\) for all \(z\), we have  
  \(f_\varepsilon(z)\neq-\varepsilon\) for every \(z\in\mathbb D\); thus \(-\varepsilon\notin f_\varepsilon(\mathbb D)\).

If a radius \(r>0\) worked for all such functions, then for any \(\varepsilon<r\) we would have  
\(-\varepsilon\in D_r(0)\) but \(-\varepsilon\notin f_\varepsilon(\mathbb D)\), impossible.  
Hence no uniform radius exists even after imposing \(f'(0)=1\).

--------------------------------------------------------------------
### (c)  Area theorem for a function with a simple pole

Let  

\[
h(z)=\frac1z+c_0+c_1z+c_2z^2+\cdots
\]

be injective on the punctured disc \(0<|z|<1\).  
For \(0<\rho<1\) consider the curve  

\[
\gamma_\rho(t)=h(\rho e^{it}),\qquad 0\le t\le2\pi .
\]

Because \(h\) is injective, \(\gamma_\rho\) is a simple closed curve; let \(A(\rho)\) be the area of its interior.  
By Green’s theorem,

\[
A(\rho)=\frac1{2i}\oint_{\gamma_\rho}\overline w\,dw
      =\frac1{2i}\oint_{|z|=\rho}\overline{h(z)}\,h'(z)\,dz .
\]

Write the Laurent expansions

\[
h(z)=z^{-1}+\sum_{k\ge0}c_kz^k,\qquad
h'(z)=-z^{-2}+\sum_{k\ge0}(k+1)c_{k+1}z^k .
\]

Then

\[
\overline{h(z)}\,h'(z)
 =\bigl(z^{-1}+\sum_{k\ge0}\overline{c_k}\,\overline{z}^{\,k}\bigr)
   \bigl(-z^{-2}+\sum_{j\ge0}(j+1)c_{j+1}z^{j}\bigr) .
\]

On the circle \(|z|=\rho\) we have \(\overline{z}=\rho^{2}/z\).  
Multiplying out and integrating termwise, only the terms where the total power of \(z\) is \(-1\) survive.  
A short computation gives

\[
\frac1{2i}\oint_{|z|=\rho}\overline{h(z)}\,h'(z)\,dz
   =\pi\Bigl(\rho^{-2}-\sum_{n\ge1}n|c_n|^{2}\rho^{2n}\Bigr).
\]

Since \(A(\rho)\ge0\),

\[
\sum_{n\ge1}n|c_n|^{2}\rho^{2n}\le\rho^{-2}\qquad(0<\rho<1).
\]

Letting \(\rho\to1^{-}\) (the left–hand side increases with \(\rho\)) yields

\[
\boxed{\displaystyle\sum_{n\ge1}n|c_n|^{2}\le1}.
\]

--------------------------------------------------------------------
### (d)  Constructing a square‑root function

Let  

\[
f(z)=z+a_2z^2+a_3z^3+\cdots
\]

be injective on \(\mathbb D\) with \(f(0)=0,\;f'(0)=1\).

Because \(f(z)/z=1+a_2z+a_3z^2+\cdots\) is holomorphic and nowhere zero on \(\mathbb D\) (its value at \(0\) is \(1\)), the simply connected domain \(\mathbb D\) admits a holomorphic square root.  
Choose \(\psi:\mathbb D\to\mathbb C\) holomorphic with  

\[
\psi^{2}(z)=\frac{f(z)}{z},\qquad \psi(0)=1 .
\]

Define  

\[
g(z)=z\,\psi(z^{2}),\qquad z\in\mathbb D .
\]

* \(g(0)=0\) and \(g'(0)=\psi(0)=1\).
* Moreover,
  \[
  g^{2}(z)=z^{2}\psi(z^{2})^{2}=z^{2}\cdot\frac{f(z^{2})}{z^{2}}=f(z^{2}).
  \]

*Injectivity of \(g\).*  
If \(g(z_{1})=g(z_{2})\) then squaring gives \(f(z_{1}^{2})=f(z_{2}^{2})\); injectivity of \(f\) implies \(z_{1}^{2}=z_{2}^{2}\), i.e. \(z_{1}= \pm z_{2}\).  
If \(z_{1}=-z_{2}\neq0\) then, using the oddness of \(g\) (which follows from \(g(-z)=-z\psi((-z)^{2})=-z\psi(z^{2})=-g(z)\)), we obtain \(g(z_{1})=-g(z_{2})\).  Hence \(g(z_{1})=g(z_{2})\) forces \(g(z_{2})=0\), which happens only at \(z_{2}=0\); consequently \(z_{1}=z_{2}=0\).  
Thus \(g\) is injective.

Therefore \(g\) satisfies the same hypotheses as \(f\).

--------------------------------------------------------------------
### (e)  The bound \(|a_{2}|\le2\) and the extremal functions

From the construction in (d),

\[
\psi(z)=1+\frac{a_{2}}{2}z+\cdots\quad\Longrightarrow\quad
\psi(z^{2})=1+\frac{a_{2}}{2}z^{2}+\cdots .
\]

Hence  

\[
g(z)=z\psi(z^{2})=z+\frac{a_{2}}{2}z^{3}+\cdots ,
\]

so \(g\) contains only odd powers of \(z\).  Consequently  

\[
\frac1{g(z)}=\frac1z\Bigl(1-\frac{a_{2}}{2}z^{2}+\cdots\Bigr)
           =\frac1z-\frac{a_{2}}{2}z+\cdots .
\]

Write  

\[
\frac1{g(z)}=\frac1z+b_{0}+b_{1}z+b_{2}z^{2}+\cdots .
\]

Because \(g\) is odd, \(1/g\) is also odd; thus \(b_{0}=b_{2}=b_{4}=\cdots=0\) and  
\(b_{1}=-\dfrac{a_{2}}{2}\).

The function \(1/g\) is of the form required in part (c): it has a simple pole at \(0\) with residue \(1\) and is injective on \(0<|z|<1\) (injectivity follows from that of \(g\)).  
Applying part (c) to \(1/g\) gives  

\[
\sum_{n\ge1}n|b_{n}|^{2}\le1\quad\Longrightarrow\quad|b_{1}|^{2}\le1 .
\]

Hence  

\[
\Bigl|\frac{a_{2}}{2}\Bigr|^{2}\le1\quad\Longrightarrow\quad|a_{2}|\le2 .
\]

*Equality case.*  
If \(|a_{2}|=2\) then \(|b_{1}|=1\) and equality in the area theorem forces  

\[
\frac1{g(z)}=\frac1z+e^{i\theta}z\qquad(\theta\in\mathbb R)
\]

(all higher coefficients vanish).  Solving for \(g\),

\[
g(z)=\frac{z}{1+e^{i\theta}z^{2}} .
\]

Now \(f(z^{2})=g(z)^{2}=\dfrac{z^{2}}{(1+e^{i\theta}z^{2})^{2}}\); replacing \(z^{2}\) by \(z\) yields  

\[
f(z)=\frac{z}{(1+e^{i\theta}z)^{2}} .
\]

Conversely, each function of this form is injective on \(\mathbb D\), satisfies \(f(0)=0,\;f'(0)=1\) and has \(a_{2}= -2e^{i\theta}\), so \(|a_{2}|=2\).  
Thus the estimate is sharp.

--------------------------------------------------------------------
### (f)  Distance between two omitted values

Let  

\[
h(z)=\frac1z+c_{0}+c_{1}z+c_{2}z^{2}+\cdots
\]

be injective on \(\mathbb D\) and suppose that it omits two (distinct) values \(z_{1},z_{2}\).  
For \(j=1,2\) set  

\[
f_{j}(z)=\frac{1}{h(z)-z_{j}} .
\]

Because \(h\) never equals \(z_{j}\), each \(f_{j}\) is holomorphic on \(\mathbb D\).  
Moreover,

* \(f_{j}(0)=0\) (since \(h(z)\sim1/z\) near \(0\)),
* \(f_{j}'(0)=1\) (a direct computation from the expansion below),
* \(f_{j}\) is injective: if \(f_{j}(z_{1})=f_{j}(z_{2})\) then  
  \(h(z_{1})-z_{j}=h(z_{2})-z_{j}\) \(\Rightarrow\) \(h(z_{1})=h(z_{2})\) \(\Rightarrow\) \(z_{1}=z_{2}\) by injectivity of \(h\).

Thus each \(f_{j}\) satisfies the hypotheses of the theorem.  
By part (e) the coefficient of \(z^{2}\) in the power series of \(f_{j}\) obeys  

\[
\bigl|a_{2}^{(j)}\bigr|\le2 .
\]

Now expand \(f_{j}\).  Write  

\[
h(z)-z_{j}= \frac1z+(c_{0}-z_{j})+c_{1}z+c_{2}z^{2}+\cdots .
\]

Hence  

\[
f_{j}(z)=\frac{1}{h(z)-z_{j}}
        =z-(c_{0}-z_{j})z^{2}+O(z^{3}),
\]

so the coefficient of \(z^{2}\) is \(a_{2}^{(j)}=-(c_{0}-z_{j})\).  
Consequently  

\[
|c_{0}-z_{j}|=\bigl|a_{2}^{(j)}\bigr|\le2\qquad(j=1,2).
\]

Finally,

\[
|z_{1}-z_{2}|
   =|(c_{0}-z_{2})-(c_{0}-z_{1})|
   \le|c_{0}-z_{2}|+|c_{0}-z_{1}|
   \le2+2=4 .
\]

Thus  

\[
\boxed{|z_{1}-z_{2}|\le4}.
\]

--------------------------------------------------------------------
### (g)  The Koebe–Bieberbach radius theorem

Let \(f:\mathbb D\to\mathbb C\) be injective, \(f(0)=0\) and \(f'(0)=1\).  
We prove that the open disc \(D_{1/4}(0)\) is always contained in \(f(\mathbb D)\) and that the radius \(1/4\) cannot be improved.

---

#### 1.  If a point \(w\) is omitted, then \(|w|\ge\frac14\).

Assume that some \(w\neq0\) satisfies \(w\notin f(\mathbb D)\).  
Because \(f\) is injective and \(f(0)=0\), we have \(f(z)\neq0\) for all \(z\neq0\); hence the function  

\[
h(z)=\frac1f(z)
\]

is holomorphic on \(\mathbb D\).  
Near the origin \(f(z)=z+O(z^{2})\), so  

\[
h(z)=\frac1z+c_{0}+c_{1}z+c_{2}z^{2}+\cdots ,
\]

i.e. \(h\) has the required Laurent expansion with residue \(1\) at the pole \(z=0\).  
Since \(f\) never takes the value \(w\), we have \(h(z)\neq\frac1w\) for every \(z\in\mathbb D\).  
Moreover, \(h(z)=0\) would imply \(f(z)=\infty\), which cannot happen because \(f\) is holomorphic; thus \(h\) omits the value \(0\) as well (on the punctured disc; at \(z=0\) we have a pole, so \(h(0)=\infty\)).  
Therefore \(h\) is injective on \(\mathbb D\) (as a map to the Riemann sphere) and omits the two values \(0\) and \(\frac1w\).

Applying part (f) to \(h\) gives  

\[
\Bigl|0-\frac1w\Bigr|\le4\quad\Longrightarrow\quad\frac1{|w|}\le4\quad\Longrightarrow\quad|w|\ge\frac14 .
\]

---

#### 2.  Every point with \(|w|<\frac14\) belongs to \(f(\mathbb D)\).

If \(|w|<\frac14\) then, by the contrapositive of the estimate just proved, \(w\) cannot be omitted by \(f\).  
Hence \(D_{1/4}(0)\subset f(\mathbb D)\).

---

#### 3.  The radius \(\frac14\) is best possible.

Consider the Koebe function  

\[
k(z)=\frac{z}{(1-z)^{2}}=z+2z^{2}+3z^{3}+\cdots .
\]

It is injective on \(\mathbb D\), satisfies \(k(0)=0,\;k'(0)=1\), and its image is \(\mathbb C\setminus(-\infty,-\frac14]\).  
In particular, \(-\frac14\notin k(\mathbb D)\).  
Thus no disc centred at the origin with radius larger than \(\frac14\) can be contained in the image of every normalized univalent function.

---

Combining the three steps we obtain the Koebe–Bieberbach theorem:

\[
\boxed{\;D_{1/4}(0)\subset f(\mathbb D)\quad\text{for every injective }f:\mathbb D\to\mathbb C
\text{ with }f(0)=0,\;f'(0)=1,\;}
\]

and the constant \(\frac14\) cannot be increased.

--------------------------------------------------------------------
**All parts (a)–(g) are now proved.** ∎

---

## Reasoning Details (raw)

```json
[
  {
    "type": "reasoning.text",
    "text": "We need to produce a full solution with proofs for each part (a)-(g). The problem statement is given. The solution skeleton is provided in the prompt, but we need to flesh out details, ensure rigorous reasoning, fill any gaps, and present a complete answer.\n\nWe need to show:\n\n(a) No uniform r exists without further restrictions. Provide sequence f_n(z)=z/n, compute f_n'(0)=1/n, show 1/n not in image, etc.\n\n(b) Even with f'(0)=1, no uniform r exists. Use f_epsilon(z)=epsilon(e^{z/epsilon} -1). Show f_epsilon(0)=0, f_epsilon'(0)=1, image omits -epsilon, so for any r>0 choose epsilon<r then -epsilon in D_r(0) but not in image.\n\n(c) For h(z)=1/z + c0 + c1 z + ... injective on punctured disc 0<|z|<1, show sum_{n>=1} n|c_n|^2 <=1. Use area theorem (Gronwall's area theorem). Compute area of complement of h(D_rho\\{0}) and let rho->1.\n\nWe need to provide proof: For injective meromorphic function on punctured disc with simple pole at 0, the area of complement of image of {0<|z|<rho} is pi(1/rho^2 - sum_{n>=1} n|c_n|^2 rho^{2n}) >=0. Then letting rho->1 gives inequality.\n\n(d) Given f(z)=z + a2 z^2 + ... injective, f(0)=0, f'(0)=1. Show there exists g injective with same normalization such that g^2(z)=f(z^2). Approach: Since f(z)/z is nowhere zero and holomorphic on D, we can define a holomorphic square root psi with psi(0)=1 (since f(z)/z = 1 + a2 z + ... nonzero at 0). Then define g(z)=z psi(z^2). Show g is injective, g(0)=0, g'(0)=1, and g^2(z)=f(z^2).\n\n(e) Using previous, show |a2| <=2, equality iff f(z)=z/(1 - e^{i theta}z)^2. Steps: Compute expansion of 1/g(z) = 1/z + b0 + b1 z + ...; note g is odd so only odd powers; relate b1 to a2; apply part (c) to 1/g to get |b1| <=1; then |a2|=2|b1| <=2. Equality case: if |b1|=1 then equality in area theorem forces 1/g(z)=1/z + e^{i theta} z, thus g(z)=z/(1+ e^{i theta} z^2). Then compute f(z)=g(z)^2 with substitution z-> sqrt? Actually we have g^2(z)=f(z^2). So f(z)= (g(sqrt(z)))^2? Wait careful: we have g^2(z) = f(z^2). So for any w, f(w) = g(sqrt(w))^2 where sqrt denotes a branch; but since both sides are even? Actually we can deduce: replace z by sqrt(z) (choose principal branch) yields f(z) = g(sqrt(z))^2. But we can also directly compute: from g(z)=z psi(z^2) and psi^2(z)=f(z)/z, we have g(z)=z sqrt{f(z)/z}? Actually psi(z) = sqrt{f(z)/z}. Then g(z) = z psi(z^2) = z sqrt{f(z^2)/z^2} = sqrt{f(z^2)}. Wait check: psi(z^2) = sqrt{f(z^2)/z^2}. Multiply by z: g(z) = z * sqrt{f(z^2)/z^2} = sqrt{f(z^2)}. So g(z)^2 = f(z^2). Good. Then if g(z) = z/(1+ e^{i theta} z^2), then g(z)^2 = z^2/(1+ e^{i theta} z^2)^2. So f(z^2) = z^2/(1+ e^{i theta} z^2)^2. Replace w = z^2: f(w) = w/(1+ e^{i theta} w)^2. So indeed f(z)=z/(1+ e^{i theta} z)^2.\n\nEquality case also includes rotation.\n\n(f) If h injective on D and avoids two values z1, z2, then |z1 - z2| <=4. Approach: Consider 1/(h(z)-z_j) which is injective, has simple pole at 0, expansion 1/z + ... ; apply part (c) to get bound on coefficient of z term; relate difference of coefficients to z1 - z2; get bound.\n\nWe need to be precise: Let h(z) injective on D, avoid z1 and z2. Then for each j, define H_j(z) = 1/(h(z)-z_j). Since h avoids z_j, denominator never zero, H_j is holomorphic on D. Moreover, H_j has a simple pole at 0? Actually h(0) may be something; but we can assume after translation that h(0)=0? The statement likely assumes h is injective on D and avoids z1, z2, but not necessarily normalized. However we can apply part (c) after subtracting a constant to make pole at 0? Usually the area theorem applies to functions of form 1/z + c0 + c1 z + ... which are injective on punctured disc. So we need to ensure H_j has that form. Since h is injective on D, h(0) is some value; but we can consider H_j(z) - 1/z? Actually we need to get expansion at 0: Since h is injective and avoids z_j, h(z)-z_j is nonzero and holomorphic, with a zero at some point? Wait h may not have zero at 0. But we can consider the function 1/(h(z)-z_j) which is holomorphic and nonzero? Actually if h avoids z_j, then h(z)-z_j never zero, so its reciprocal is holomorphic and nonzero? No, it's holomorphic and never zero, but may have a zero at infinity? Not needed. To get a simple pole at 0, we need h(z)-z_j to have a simple zero at 0. So we need to assume h(0)=z_j? That seems not given. However typical proof of Koebe 1/4 theorem uses that if f omits w, then 1/f omits 0 and 1/w, and 1/f has a simple pole at 0 because f(0)=0 and f'(0)=1 => near 0, f(z)=z+..., so 1/f(z)=1/z + ... . So in part (f) we likely consider h injective on D and avoids z1, z2, and also h(0)=0? Actually the statement: \"If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, show that |z1 - z2| <= 4.\" Wait they already gave the form of h: h(z) = 1/z + c0 + c1 z + ... . So h already has a simple pole at 0 with residue 1. So they assume h is of that form (i.e., meromorphic on D with simple pole at 0, residue 1). And h is injective on D (including at 0? Actually it's meromorphic, injective as a map from D\\{0} to C). So we can directly apply part (c) to h and to h - (z1+z2)/2? Hmm.\n\nBut the hint: \"Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\" So we consider H_j(z) = 1/(h(z) - z_j). Since h has pole at 0, h(z)-z_j also has pole at 0 (same principal part). Its reciprocal then has a zero at 0? Let's compute: If h(z) = 1/z + c0 + c1 z + ..., then near 0, h(z)-z_j = 1/z + (c0 - z_j) + c1 z + ... . Its reciprocal: 1/(h(z)-z_j) = z / [1 + (c0 - z_j) z + c1 z^2 + ...] = z * [1 - (c0 - z_j) z + ...] = z - (c0 - z_j) z^2 + ... . So expansion: H_j(z) = z + d0 + d1 z + ...? Actually we see that H_j(z) has a zero at 0 (no pole). Its expansion starts with z term. So it's holomorphic at 0 with zero of order 1. Then we can consider K_j(z) = 1/H_j(z) = h(z)-z_j, which has pole at 0. But part (c) applies to functions with simple pole at 0 and residue 1. So we might instead consider 1/H_j(z) = h(z)-z_j, which has pole at 0 but residue 1? Let's check: h(z)-z_j = 1/z + (c0 - z_j) + c1 z + ... . So indeed it has simple pole at 0 with residue 1. So h(z)-z_j is of the form required in part (c). And it's injective? Since h is injective and subtracting constant z_j doesn't affect injectivity, h(z)-z_j is injective on D\\{0}. So we can apply part (c) to the function h(z)-z_j. Then we get sum_{n>=1} n|d_n|^2 <= 1 where d_n are coefficients in expansion of h(z)-z_j = 1/z + d0 + d1 z + d2 z^2 + ... . Here d0 = c0 - z_j, d1 = c1, etc. So the bound applies to the coefficients d_n for n>=1: sum n|d_n|^2 <=1. In particular, |d1| <=1. So |c1| <=1 for each j? Wait d1 = c1 (since subtracting constant doesn't affect z coefficient). So we get |c1| <=1. That seems too weak to get |z1 - z2| <=4. Actually we need to use both j=1,2 to get bound on difference.\n\nMaybe we consider the difference of the two functions: (h(z)-z1) - (h(z)-z2) = z2 - z1, constant. Not helpful.\n\nAlternate approach: Consider the function H(z) = 1/(h(z)-z1) - 1/(h(z)-z2). This equals (z2 - z1)/[(h(z)-z1)(h(z)-z2)]. Might be easier to bound.\n\nBut hint says: Look at second coefficient in power series expansion of 1/(h(z)-z_j). So they consider expansion of 1/(h(z)-z_j) around 0. As we computed, 1/(h(z)-z_j) = z - (c0 - z_j) z^2 + ... . So the coefficient of z^2 is -(c0 - z_j). The second coefficient (maybe meaning coefficient of z) is 1? Actually series: a_{-1}? Wait they'd write expansion in powers of z: 1/(h(z)-z_j) = A_{-1} z^{-1} + A_0 + A_1 z + ...? But we found it's holomorphic at 0, so no negative powers. Let's recompute carefully:\n\nh(z) = 1/z + c0 + c1 z + c2 z^2 + ...\n\nThen h(z) - z_j = 1/z + (c0 - z_j) + c1 z + c2 z^2 + ...\n\nWe want to compute its reciprocal: 1/(h(z)-z_j). Let w = h(z)-z_j. Write w = (1/z) * [1 + (c0 - z_j) z + c1 z^2 + c2 z^3 + ...]. So w = (1/z) * (1 + alpha_1 z + alpha_2 z^2 + ...), where alpha_1 = c0 - z_j, alpha_2 = c1, etc.\n\nThen 1/w = z * (1 + alpha_1 z + alpha_2 z^2 + ...)^{-1} = z * [1 - alpha_1 z + (alpha_1^2 - alpha_2) z^2 + ...].\n\nThus 1/(h(z)-z_j) = z - alpha_1 z^2 + (alpha_1^2 - alpha_2) z^3 + ... .\n\nSo expansion: = z + b0 + b1 z + b2 z^2 + ...? Actually there is no constant term; the series starts with z term. So we can write:\n\n1/(h(z)-z_j) = z + A_0 + A_1 z + A_2 z^2 + ...? Wait that seems off: If we factor z, we have z * (1 + A_1 z + A_2 z^2 + ...). So the series is z + A_1 z^2 + A_2 z^3 + ... . So there is no term independent of z (i.e., z^0). So the coefficient of z^0 is 0. The coefficient of z^1 is 1. The coefficient of z^2 is A_1 = -(c0 - z_j). The coefficient of z^3 is A_2 = (c0 - z_j)^2 - c1, etc.\n\nThus the \"second coefficient\" likely refers to the coefficient of z^2 (i.e., the coefficient after the leading term). So that coefficient is -(c0 - z_j). Then applying part (c) to the function 1/(h(z)-z_j) ??? But part (c) applies to functions of form 1/z + c0 + c1 z + ... injective on punctured disc. However 1/(h(z)-z_j) is holomorphic at 0 (has a zero), not of that form. So we cannot directly apply (c). Instead we might consider its reciprocal, which is h(z)-z_j, which is of the right form. Then the coefficient of z in h(z)-z_j is c1. So applying (c) gives |c1| <= 1. That doesn't involve z_j.\n\nThus we need a different approach: Maybe we consider the function H(z) = 1/(h(z)-z1) + 1/(h(z)-z2). Its expansion might give something like 2/z + ... and then apply (c) to get bound on something like (z1+z2). Hmm.\n\nLet's recall known proof of Koebe 1/4 theorem: If f omits w, then consider F(z) = 1/f(z) - 1/w. This function omits 0 and -1/w? Actually standard proof: Suppose f omits w \u2260 0. Then g(z) = w f(z)/(w - f(z)) is univalent, normalized, and omits 0. Then apply area theorem to g'(z) or something. Another approach: Use that if f omits w, then the function h(z) = 1/f(z) - 1/w is univalent and omits 0 and something, then apply area theorem to get bound on |w|.\n\nBut the problem's part (f) is a lemma: If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, then |z1 - z2| <= 4. This is a known result: If a univalent function on the unit disk (with normalization 1/z + ... ) omits two values, then the distance between those omitted values is at most 4. This is used to prove Koebe 1/4: If f omits w, then 1/f omits 0 and 1/w, apply the lemma with z1=0, z2=1/w to get |1/w| <= 4 => |w| >= 1/4.\n\nThus we need to prove the lemma. Let's attempt to prove it.\n\nLet h(z) = 1/z + c0 + c1 z + c2 z^2 + ... be injective on D (i.e., univalent on D\\{0}? Actually h is meromorphic with simple pole at 0, injective on D). Suppose h omits two distinct values a and b (I'll use z1, z2). Consider the function\n\nH(z) = \\frac{1}{h(z) - a} - \\frac{1}{h(z) - b}.\n\nCompute H(z) = \\frac{b - a}{(h(z)-a)(h(z)-b)}.\n\nSince h omits a and b, denominator never zero, so H is holomorphic on D. Moreover, as z\u21920, h(z) ~ 1/z, so h(z)-a ~ 1/z, h(z)-b ~ 1/z, thus product ~ 1/z^2, so H(z) ~ (b-a) z^2. So H has a zero of order at least 2 at z=0. Actually we can compute expansion: h(z) = 1/z + c0 + c1 z + ...; then\n\n1/(h(z)-a) = z - (c0 - a) z^2 + O(z^3)\n1/(h(z)-b) = z - (c0 - b) z^2 + O(z^3)\n\nSubtract: H(z) = [(c0 - b) - (c0 - a)] z^2 + O(z^3) = (a - b) z^2 + O(z^3). So H(z) = (a - b) z^2 + higher order.\n\nThus H(z)/z^2 is holomorphic at 0 with value (a - b) at 0.\n\nNow consider the function G(z) = H(z)/z^2. Then G is holomorphic on D, G(0) = a - b.\n\nWe want to bound |a - b| using area theorem applied to something like 1/G? Not sure.\n\nAlternatively, consider the function\n\nF(z) = \\frac{1}{h(z) - a} + \\frac{1}{h(z) - b}.\n\nIts expansion: sum = 2z - (2c0 - a - b) z^2 + O(z^3). So F(z)/z = 2 - (2c0 - a - b) z + ... . So F(z)/z is holomorphic, nonzero at 0? Its value at 0 is 2.\n\nMaybe we can apply area theorem to the function\n\n\\phi(z) = \\frac{1}{F(z)} ?\n\nLet's think: We want to bound |a-b|. Known proof: If h omits a and b, then consider the function\n\n\\phi(z) = \\frac{h(z) - a}{h(z) - b}.\n\nThis maps D into C \\ {0,1} (since h omits a,b, the ratio never equals 0 or \u221e? Actually if h(z) = a then numerator zero => ratio 0, but h omits a so numerator never zero; if h(z) = b then denominator zero => ratio \u221e, but h omits b so denominator never zero; thus ratio omits 0 and \u221e, i.e., takes values in C\\{0,\u221e} = C*? Actually omitting 0 and \u221e means it's nonzero and finite, i.e., maps into C\\{0}. But also it never equals 1? If h(z) = something else? Actually ratio =1 when h(z)-a = h(z)-b => a=b, which is false. So ratio never equals 1 either? Wait solve (h-a)/(h-b)=1 => h-a = h-b => -a = -b => a=b, contradiction. So ratio omits 1 as well. So the ratio omits three values: 0,1,\u221e. By Picard's theorem, a meromorphic function on D omitting three values is constant. But h is not necessarily meromorphic on whole D? It is meromorphic with a pole at 0, but ratio may be analytic? Let's check: (h-a)/(h-b) is meromorphic on D, with possible poles where h=b (but h omits b, so no poles), zeros where h=a (but h omits a, so no zeros). So it's holomorphic and nonzero on D. Moreover, as z\u21920, h(z) ~ 1/z, so (h-a)/(h-b) ~ (1/z)/(1/z) = 1. So it tends to 1 at 0. So it's a holomorphic function on D that never takes values 0,1,\u221e (i.e., never 0 or 1, and finite nonzero). Actually it's holomorphic and never 0, and its reciprocal is also holomorphic (since never \u221e). So it's a holomorphic map from D to C\\{0,1}. By Picard's little theorem, a holomorphic function from D to C omitting two values is constant. Here we omit 0 and 1, so it must be constant. Since its limit at 0 is 1, the constant must be 1. Therefore (h-a)/(h-b) \u2261 1, implying a=b, contradiction unless the omitted values are not distinct. Wait this suggests that a meromorphic function on D omitting three values must be constant, but we only omitted two values (0 and 1) for the ratio; we also omitted \u221e implicitly because it's holomorphic (no poles). So indeed we omitted three values: 0,1,\u221e. So by Picard, the ratio is constant. Since limit at 0 is 1, constant =1, giving a=b. So if h omits two distinct values a,b, then the ratio (h-a)/(h-b) is a holomorphic function on D omitting 0,1,\u221e, thus constant, leading to a=b. Therefore h cannot omit two distinct values unless it's constant? But h is not constant because it has a pole at 0. Something is off: The ratio (h-a)/(h-b) is holomorphic on D? Let's check: h is meromorphic with a simple pole at 0. At z=0, h has a pole, so h-a and h-b also have poles. Their ratio near 0: (1/z + ... - a)/(1/z + ... - b) = (1/z (1 + (c0 - a)z + ...))/(1/z (1 + (c0 - b)z + ...)) = (1 + (c0 - a)z + ...)/(1 + (c0 - b)z + ...). This is holomorphic at 0 and equals 1 at z=0. So indeed the ratio extends holomorphically to 0. So the ratio is holomorphic on all of D. It never takes value 0 because numerator never zero (h omits a). It never takes value \u221e because denominator never zero (h omits b). It never takes value 1 because that would imply a=b. So it omits three values 0,1,\u221e. By Picard's theorem, a holomorphic function on D omitting three values is constant. Since its value at 0 is 1, it's identically 1. Therefore (h-a)/(h-b) \u2261 1 => h-a \u2261 h-b => a=b. So indeed a non-constant meromorphic function on D with a simple pole at 0 cannot omit two distinct values. Wait but we know the Koebe function omits -1/4 only one value. So indeed it cannot omit two values. This seems to prove that if h omits two values, then it must be constant, which contradicts the pole. Therefore the lemma statement \"If h is injective on D and avoids the values z1 and z2, then |z1 - z2| <= 4\" is vacuously true? Actually if h omits two values, then it must be constant, which cannot happen because of the pole, so the hypothesis cannot be satisfied unless the omitted values are equal? But the lemma likely intends that h omits the values z1 and z2 (i.e., does not take those values) but may still be non-constant; the conclusion is that the distance between them is at most 4. This is a known result: If a univalent function on the unit disk (with normalization f(z)=z+... ) omits two values, then those values lie within distance 4 of each other. Actually the standard lemma: If f is univalent in D and omits the values a and b, then |a-b| \u2264 4. This is used in the proof of Koebe 1/4 theorem via considering g(z) = f(z)/(f(z)-w) etc. Wait I recall a lemma: If f is univalent in D and f(0)=0, f'(0)=1, and f omits w, then |w| \u2265 1/4. The proof uses the function F(z) = z f'(z)/(f(z)-w). Something like that.\n\nBut the problem's part (f) is stated as: If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, then |z1 - z2| \u2264 4. The hint: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j). So they want to use part (c) on the functions 1/(h(z)-z_j). Let's try to make that work.\n\nLet H_j(z) = 1/(h(z)-z_j). As we computed, H_j(z) = z - (c0 - z_j) z^2 + O(z^3). So H_j(z) is holomorphic on D, with a zero at 0 of order 1 (since leading term z). So we can consider the function K_j(z) = H_j(z)/z = 1 - (c0 - z_j) z + O(z^2). This is holomorphic and nonzero at 0 (value 1). Then we can apply part (c) to something like 1/K_j? Actually 1/K_j(z) = z/H_j(z) = h(z)-z_j, which has the form 1/z + (c0 - z_j) + c1 z + ... . So 1/K_j(z) is of the form required in part (c). And it's injective? Since h is injective, subtracting constant doesn't affect injectivity, so h(z)-z_j is injective on D\\{0}. So we can apply part (c) to the function h(z)-z_j. That yields sum_{n>=1} n|d_n|^2 \u2264 1 where d_n are coefficients of h(z)-z_j = 1/z + d0 + d1 z + d2 z^2 + ... . Here d0 = c0 - z_j, d1 = c1, d2 = c2, etc. So we get |c1| \u2264 1 (since n=1 term gives 1*|c1|^2 \u2264 sum \u2264 1). So |c1| \u2264 1. That's independent of j. So we get a bound on c1, not on z1 - z2.\n\nBut maybe we need to consider the difference of the two functions h(z)-z1 and h(z)-z2. Their difference is constant (z2 - z1). Not helpful.\n\nAlternatively, consider the product? Hmm.\n\nLet's search memory: There is a known lemma: If p(z) = 1/z + \u03b20 + \u03b21 z + ... is univalent in D, then |\u03b21| \u2264 1. That's exactly part (c) with n=1. So we have |c1| \u2264 1. Then if h omits z1 and z2, we can consider the function\n\n\u03c6(z) = \\frac{h(z) - z1}{h(z) - z2}.\n\nAs argued, this omits 0,1,\u221e, thus constant. But wait, we need to check that \u03c6 is holomorphic on D. h is meromorphic with a simple pole at 0; h - z1 and h - z2 also have simple poles at 0. Their ratio is holomorphic at 0 as we saw. It may have zeros or poles where numerator or denominator zero, but those correspond to h = z1 or h = z2, which are omitted, so no zeros or poles. So \u03c6 is holomorphic and nonzero on D. Moreover, \u03c6(0) = 1 (since both numerator and denominator have same leading term 1/z). So \u03c6 is a holomorphic function on D omitting 0 and 1 (since it never equals 0 or 1). Actually does it ever equal \u221e? No, because denominator never zero. So it omits 0,1,\u221e. By Picard, \u03c6 is constant. Since \u03c6(0)=1, \u03c6 \u2261 1. Therefore h(z)-z1 \u2261 h(z)-z2 => z1 = z2. So the only way h can omit two values is if they are equal. Thus the hypothesis that h omits two distinct values cannot happen unless h is constant? But h is not constant because of pole. So the lemma is vacuously true: If h omits two values, then they must be equal, so |z1 - z2| = 0 \u2264 4. But the lemma likely expects a nontrivial bound for the case where h omits two values (maybe allowing h to be meromorphic with a pole at 0 but not necessarily injective? Actually they said injective). The Picard argument shows that any meromorphic function on D omitting three values is constant. Here we have a meromorphic function h with a simple pole at 0; if it omits two values, then the function (h - z1)/(h - z2) omits 0,1,\u221e, thus constant, leading to z1=z2. So indeed a non-constant meromorphic function on D cannot omit two distinct values. So the lemma is true but trivial: the hypothesis forces z1=z2, so the conclusion holds. However, the problem likely expects a nontrivial proof using area theorem, not Picard. Perhaps they want to avoid using Picard and instead use area theorem to get a quantitative bound that yields the constant 4, which is sharp (the Koebe function omits -1/4 only one value, but if we consider two omitted values, the maximum distance is 4, attained when the omitted values are 2 and -2? Actually consider the function h(z) = 1/z + c0. This omits infinity? Not sure. Let's test: h(z) = 1/z + c0. This is injective? For nonzero c0, it's a M\u00f6bius transformation: h(z) = (1 + c0 z)/z. This is injective on D\\{0}? It's a linear fractional transformation, injective on its domain (the Riemann sphere). It omits the value c0? Actually solve h(z) = w => (1 + c0 z)/z = w => 1 + c0 z = w z => 1 = (w - c0) z => z = 1/(w - c0). This has a solution in D if |1/(w - c0)| < 1 => |w - c0| > 1. So h omits the disk of radius 1 centered at c0? Actually the image is {w: |w - c0| > 1} \u222a {\u221e}? Wait as z\u21920, h(z)\u2192\u221e; as z\u2192\u221e? Not relevant. So h omits the closed disk of radius 1 around c0? Actually the equation gives a unique z for each w \u2260 c0; that z lies in D iff |w - c0| > 1. So the image of D\\{0} under h is {w: |w - c0| > 1} \u222a {\u221e}. So h omits the open disk of radius 1 around c0. So it omits infinitely many values, not just two. So the hypothesis of omitting two values is very weak; many functions omit many values. So the lemma must be nontrivial: If a univalent function (with pole at 0) omits two specific values, then those values cannot be too far apart. For example, the function h(z) = 1/z omits 0 and \u221e? Actually h(z)=1/z omits 0? No, h(z)=1/z takes all nonzero values; it omits 0 and \u221e? As z\u21920, h\u2192\u221e, so \u221e is attained as a limit but not as a value? In meromorphic functions, \u221e is allowed as a value at poles. So h(z)=1/z has a pole at 0, so it attains \u221e at z=0. So it omits 0 only. So it omits one value. To omit two values, we need something like h(z) = 1/z + c, which omits a disk of radius 1 around c, thus omits infinitely many values. So the hypothesis is satisfied for many functions. The lemma then gives a bound on the distance between any two omitted values: they must lie within distance 4 of each other. For h(z)=1/z + c, the omitted set is the disk |w - c| \u2264 1. Any two points in that disk have distance at most 2. So the bound 4 is not sharp for this example; but there may be functions where the omitted set is exactly two points? Actually can a univalent function omit exactly two values? Possibly yes, e.g., a covering map of the sphere minus two points? But on the disk, maybe not. The extremal case for the lemma likely gives distance 4, achieved by some function that omits two values exactly at distance 4, like the function h(z) = 1/z + 2/z^2? Not sure.\n\nNevertheless, we need to produce a proof using area theorem as hinted. Let's try to derive bound on |z1 - z2| from the coefficients.\n\nWe have h(z) = 1/z + c0 + c1 z + c2 z^2 + ... injective.\n\nDefine A_j(z) = 1/(h(z) - z_j). As computed, A_j(z) = z - (c0 - z_j) z^2 + O(z^3). So A_j(z)/z = 1 - (c0 - z_j) z + O(z^2). So log(A_j(z)/z) is holomorphic near 0.\n\nAlternatively, consider the function B_j(z) = 1/A_j(z) = h(z) - z_j = 1/z + (c0 - z_j) + c1 z + ... . This is of the form required in part (c). So we have sum_{n>=1} n|d_n^{(j)}|^2 \u2264 1 where d_n^{(j)} are coefficients of B_j(z). In particular, |c1| \u2264 1 (since d_1^{(j)} = c1). So we get |c1| \u2264 1.\n\nNow consider the difference B_1(z) - B_2(z) = (h(z)-z1) - (h(z)-z2) = z2 - z1, a constant. So the difference of the two functions is constant. Write B_j(z) = 1/z + \u03b20^{(j)} + \u03b21 z + \u03b22 z^2 + ... where \u03b20^{(j)} = c0 - z_j, \u03b21 = c1, \u03b22 = c2, etc. So B_1(z) - B_2(z) = (\u03b20^{(1)} - \u03b20^{(2)}) = (c0 - z1) - (c0 - z2) = z2 - z1. So the constant difference is z2 - z1.\n\nNow we can apply part (c) to each B_j to get bounds on their coefficients. In particular, we have |\u03b21| = |c1| \u2264 1. Also we have sum_{n>=1} n|\u03b2_n^{(j)}|^2 \u2264 1.\n\nNow consider the function C(z) = B_1(z) + B_2(z). Its expansion: C(z) = 2/z + 2c0 - (z1+z2) + 2c1 z + 2c2 z^2 + ... . Not sure.\n\nMaybe we can consider the function D(z) = B_1(z) * B_2(z). Its expansion will involve terms like 1/z^2 etc. Then apply area theorem to something like sqrt(D)? Not sure.\n\nAlternatively, consider the function E(z) = 1/(B_1(z) B_2(z)). Since B_j(z) = h(z)-z_j, and h omits z1 and z2, we have B_j(z) \u2260 0. So E(z) is holomorphic on D. Moreover, as z\u21920, B_j(z) ~ 1/z, so E(z) ~ z^2. So E has a zero of order 2 at 0. Then we can consider F(z) = sqrt(E(z))? Choose a branch of sqrt such that F(z) ~ z near 0. Then F(z) is holomorphic, injective? Not sure.\n\nBut the hint says: Look at the second coefficient in the power series expansion of 1/(h(z) - z_j). That is A_j(z). So they want to examine the coefficient of z^2 in A_j(z), which is -(c0 - z_j). Then maybe apply part (c) to something like 1/A_j(z) - 1/z? Let's see.\n\nWe have A_j(z) = z - (c0 - z_j) z^2 + O(z^3). So define C_j(z) = A_j(z)/z = 1 - (c0 - z_j) z + O(z^2). Then C_j(z) is holomorphic and nonzero at 0 (value 1). Then consider D_j(z) = 1/C_j(z) = z/A_j(z) = h(z)-z_j = 1/z + (c0 - z_j) + c1 z + ... . So we are back.\n\nMaybe we can apply part (c) to the function (A_j(z))/z? That is C_j(z). But C_j(z) is holomorphic and nonzero at 0, not of the form 1/z + ... . However we could consider its reciprocal, which is B_j(z). So we already did.\n\nThus the hint might be misinterpreted: The \"second coefficient\" might refer to the coefficient of z in the expansion of 1/(h(z)-z_j) after factoring out the leading term 1/z? Let's check: If we write 1/(h(z)-z_j) = (1/z) * something? Actually we earlier wrote h(z)-z_j = (1/z)*(1 + (c0 - z_j)z + c1 z^2 + ...). Then its reciprocal is z * (1 + (c0 - z_j)z + c1 z^2 + ...)^{-1} = z - (c0 - z_j) z^2 + ... . So the expansion of 1/(h(z)-z_j) starts with z term. So the \"second coefficient\" could be the coefficient of z^2, which is -(c0 - z_j). Then we can apply part (c) to the function (1/(h(z)-z_j))/z? That gives 1 - (c0 - z_j)z + ... . Its derivative at 0 is -(c0 - z_j). Not sure.\n\nAlternatively, maybe they want to apply part (c) to the function (1/(h(z)-z_j))'? Let's compute derivative: d/dz [1/(h(z)-z_j)] = -h'(z)/(h(z)-z_j)^2. Not helpful.\n\nLet's step back and think about the known proof of Koebe 1/4 theorem using the area theorem. The standard proof goes: Suppose f is univalent, f(0)=0, f'(0)=1, and f omits w \u2260 0. Define F(z) = z f'(z)/(f(z)-w). Show that F is univalent in D, F(0)=1, and F omits 0. Then apply the area theorem to F' or something to get |w| \u2265 1/4. Actually there is a known lemma: If p(z) = 1 + p1 z + p2 z^2 + ... is univalent in D and has positive real part, then |p1| \u2264 2. That's related.\n\nBut the problem's structure: (c) proves area theorem bound for functions with simple pole at 0. (d) constructs g such that g^2(z)=f(z^2). (e) uses that to bound a2. (f) uses the bound on a2 to get a bound on omitted values distance. (g) completes the proof.\n\nThus (f) likely uses the result from (e) that |a2| \u2264 2 for normalized univalent functions. Then they consider some transformation to get a bound on omitted values.\n\nLet's try to reconstruct: Suppose h(z) = 1/z + c0 + c1 z + ... is injective on D and omits z1 and z2. Consider the function\n\nH(z) = \\frac{1}{h(z) - z1} - \\frac{1}{h(z) - z2}.\n\nAs we computed, H(z) = (z2 - z1) + higher order terms? Actually we computed H(z) = (a - b) z^2 + ...? Wait we computed difference of reciprocals gave (a - b) z^2 + ... . Let's recompute carefully:\n\nLet A(z) = 1/(h(z)-z1), B(z) = 1/(h(z)-z2). Then\n\nA(z) = z - (c0 - z1) z^2 + O(z^3)\nB(z) = z - (c0 - z2) z^2 + O(z^3)\n\nThus A(z) - B(z) = [-(c0 - z1) + (c0 - z2)] z^2 + O(z^3) = (z1 - z2) z^2 + O(z^3). So\n\nA(z) - B(z) = (z1 - z2) z^2 + O(z^3).\n\nThus (A(z) - B(z))/z^2 = (z1 - z2) + O(z). So the function\n\n\u03a6(z) = (A(z) - B(z))/z^2\n\nis holomorphic on D (since numerator has zero of order at least 2 at 0) and \u03a6(0) = z1 - z2.\n\nNow, can we relate \u03a6 to something like derivative of a univalent function? Note that A(z) = 1/(h(z)-z1) and B(z) = 1/(h(z)-z2). Both A and B are holomorphic on D (since h omits z1,z2). Moreover, they are injective? Not necessarily.\n\nBut maybe we can consider the function\n\n\u03a8(z) = \\frac{A(z)}{B(z)} = \\frac{h(z)-z2}{h(z)-z1}.\n\nThis omits 0, \u221e, and 1? Actually as before, it omits 0 and \u221e because numerator and denominator never zero. It also omits 1 because that would imply z1=z2. So \u03a8 omits three values, thus constant by Picard, leading to z1=z2. So again trivial.\n\nThus the area theorem approach must avoid Picard and give a quantitative bound.\n\nLet's search memory: There is a known result: If p(z) = 1 + p1 z + p2 z^2 + ... is univalent in D and has positive real part, then |p1| \u2264 2. This is proved via area theorem applied to something like z p'(z)/p(z). The Koebe 1/4 theorem can be derived from this: If f omits w, then the function p(z) = (w + f(z))/(w - f(z)) has positive real part and is univalent, etc.\n\nBut the problem's (f) is likely a step towards that: If h omits z1 and z2, then consider the function\n\n\u03c6(z) = \\frac{h(z) - z1}{h(z) - z2}.\n\nThis maps D into C \\ {0,1,\u221e}. By Picard, it's constant, but we want to avoid Picard and instead use area theorem to get a bound on the distance between z1 and z2. Perhaps we can consider the logarithm of \u03c6, which is holomorphic (since \u03c6 omits 0 and \u221e) and then bound its derivative at 0 using area theorem applied to something like exp? Not sure.\n\nAlternatively, consider the function\n\n\u03c7(z) = \\frac{1}{h(z) - z1} + \\frac{1}{h(z) - z2}.\n\nIts expansion: \u03c7(z) = 2z - (2c0 - z1 - z2) z^2 + O(z^3). So \u03c7(z)/z = 2 - (2c0 - z1 - z2) z + O(z^2). So the function\n\n\u03c8(z) = \u03c7(z)/z\n\nis holomorphic, \u03c8(0)=2. Moreover, \u03c8 omits something? Since h omits z1 and z2, the denominators never zero, so \u03c7 is holomorphic and never zero? Actually \u03c7 could be zero? Possibly. But maybe we can consider 1/\u03c8(z) and apply area theorem.\n\nLet's compute 1/\u03c8(z) = z/\u03c7(z). As z\u21920, \u03c7(z) ~ 2z, so 1/\u03c8(z) ~ z/(2z) = 1/2. So 1/\u03c8 is holomorphic at 0 with value 1/2. Not helpful.\n\nMaybe we should consider the function\n\n\u03b7(z) = \\frac{h(z) - z1}{h(z) - z2} - 1 = \\frac{z2 - z1}{h(z) - z2}.\n\nThis is holomorphic (since denominator never zero) and omits 0? Actually \u03b7(z) = 0 iff numerator zero => z2=z1, which we assume distinct, so \u03b7 never zero. Also \u03b7(z) = \u221e? No, denominator never zero. So \u03b7 omits 0 and \u221e. So 1/\u03b7 is holomorphic and omits 0 and \u221e? Actually 1/\u03b7 = (h(z)-z2)/(z2 - z1). This is just a scaled version of h(z)-z2, which omits 0? Wait h(z)-z2 omits 0 because h omits z2. So 1/\u03b7 omits 0 as well. So 1/\u03b7 omits 0 and \u221e? Actually 1/\u03b7 is holomorphic and never zero (since h(z)-z2 never zero). It may have poles? No, it's holomorphic. So 1/\u03b7 omits 0 and \u221e? It never takes 0, and as a holomorphic function on D, it cannot have an essential singularity at boundary? But it's holomorphic, so it never equals \u221e (since \u221e is not a value in C). So 1/\u03b7 omits 0 only. Not helpful.\n\nLet's step back and think about the area theorem proof for the bound on omitted values. Suppose f is univalent, f(0)=0, f'(0)=1, and f omits w. Consider the function\n\nF(z) = \\frac{z f'(z)}{f(z) - w}.\n\nOne can show that F is univalent in D, F(0)=1, and F omits 0. Then apply the area theorem to F' or to something like (F(z)-1)/z to get a bound on w.\n\nActually, there is a known proof: If f omits w, then the function\n\ng(z) = \\frac{f(z)}{w - f(z)}\n\nis univalent, g(0)=0, g'(0) = -1/w, and g omits 0. Then normalize to get a function with derivative 1 at 0, apply the bound on a2 to get |w| \u2265 1/4.\n\nLet's try: Suppose f omits w \u2260 0. Define\n\ng(z) = \\frac{w f(z)}{w - f(z)}.\n\nThen g(0)=0. Compute g'(0): g(z) = w f(z) * (w - f(z))^{-1}. At 0, f(z)=z+..., so w - f(z) = w - z - ... . Expand (w - f(z))^{-1} = w^{-1} (1 - f(z)/w)^{-1} = w^{-1} (1 + f(z)/w + ...). So g(z) = w f(z) * w^{-1} (1 + f(z)/w + ...) = f(z) (1 + f(z)/w + ...) = f(z) + f(z)^2/w + ... . Since f(z)=z+..., we get g(z) = z + (1/w + a2) z^2 + ...? Let's compute precisely: f(z) = z + a2 z^2 + a3 z^3 + ... . Then f(z)^2 = z^2 + 2 a2 z^3 + ... . So g(z) = f(z) + f(z)^2/w + ... = (z + a2 z^2 + ...) + (1/w)(z^2 + 2 a2 z^3 + ...) + ... = z + (a2 + 1/w) z^2 + ... . So g'(0)=1, g(z) = z + b2 z^2 + ... with b2 = a2 + 1/w.\n\nNow g is univalent? Need to check: The map z -> w f(z)/(w - f(z)) is a composition of f with a M\u00f6bius transformation that maps the omitted value w to \u221e and 0 to 0. Since f is univalent and omits w, the M\u00f6bius transformation is injective on the image of f, so g is univalent. Also g(0)=0, g'(0)=w f'(0)/(w - f(0))^2? Actually derivative formula: g(z) = w f(z)/(w - f(z)). Differentiate: g' = [w f'(z)(w - f(z)) + w f(z) f'(z)]/(w - f(z))^2 = w w f'(z)/(w - f(z))^2? Let's compute: numerator: w f'(z)(w - f(z)) + w f(z) f'(z) = w f'(z)[w - f(z) + f(z)] = w f'(z) w = w^2 f'(z). Denominator: (w - f(z))^2. So g'(z) = w^2 f'(z)/(w - f(z))^2. At z=0, f(0)=0, f'(0)=1, so g'(0) = w^2 * 1 / w^2 = 1. Good.\n\nThus g is a normalized univalent function (holomorphic, injective, g(0)=0, g'(0)=1). Moreover, g omits 0? Check: g(z)=0 iff numerator w f(z)=0 => f(z)=0 => z=0 (since f injective and f(0)=0). So g(z)=0 only at z=0, but 0 is in the domain; however we consider omitted values in the image of g on D\\{0}? Actually g(0)=0, so 0 is attained. But we want g to omit 0? Wait we want to apply the bound on a2 to g, which requires g to be univalent and normalized. It does not need to omit anything. So we can directly apply part (e) to g to get |b2| \u2264 2. That gives |a2 + 1/w| \u2264 2. Since we also have from part (e) that |a2| \u2264 2 for f, we can combine to get a bound on w. Indeed, triangle inequality: |1/w| = |b2 - a2| \u2264 |b2| + |a2| \u2264 2 + 2 = 4, so |w| \u2265 1/4. This yields Koebe 1/4 theorem.\n\nThus part (f) might be a lemma that if h omits z1 and z2, then |z1 - z2| \u2264 4, which is analogous to the bound we just derived: For g above, we had |b2| \u2264 2 and |a2| \u2264 2, leading to |1/w| \u2264 4. In that context, z1 and z2 correspond to 0 and 1/w? Let's see: In the proof, we considered f omits w. Then we looked at 1/f omits 0 and 1/w. So h = 1/f has the form 1/z + ... and omits 0 and 1/w. Then applying (f) to h with z1=0, z2=1/w gives |1/w - 0| \u2264 4 => |w| \u2265 1/4. So indeed (f) is exactly the statement: If h(z) = 1/z + c0 + c1 z + ... is injective on D and omits two values z1 and z2, then |z1 - z2| \u2264 4.\n\nThus we need to prove (f) using the bound on a2 from (e). How can we get that? Let's try to derive (f) from (e). Suppose h(z) = 1/z + c0 + c1 z + ... is injective on D and omits z1 and z2. Consider the function\n\nH(z) = \\frac{1}{h(z) - z1} - \\frac{1}{h(z) - z2}.\n\nAs we computed, H(z) = (z1 - z2) z^2 + O(z^3). So H(z)/z^2 = (z1 - z2) + O(z). So the function\n\n\u03c6(z) = \\frac{H(z)}{z^2}\n\nis holomorphic on D, \u03c6(0) = z1 - z2.\n\nNow, can we relate \u03c6 to something like derivative of a univalent function? Note that\n\nH(z) = \\frac{1}{h(z)-z1} - \\frac{1}{h(z)-z2} = \\frac{(h(z)-z2) - (h(z)-z1)}{(h(z)-z1)(h(z)-z2)} = \\frac{z1 - z2}{(h(z)-z1)(h(z)-z2)}.\n\nThus\n\n\u03c6(z) = \\frac{z1 - z2}{z^2 (h(z)-z1)(h(z)-z2)}.\n\nSo\n\n\\frac{1}{\u03c6(z)} = \\frac{z^2 (h(z)-z1)(h(z)-z2)}{z1 - z2}.\n\nNow, consider the function\n\n\u03c8(z) = z \\sqrt{ \\frac{(h(z)-z1)(h(z)-z2)}{z1 - z2} } ?\n\nNot sure.\n\nAlternatively, consider the function\n\nF(z) = \\frac{z}{h(z)-z1} + \\frac{z}{h(z)-z2}.\n\nIts expansion: F(z) = 2 - (2c0 - z1 - z2) z + O(z^2). So F(z) is holomorphic, F(0)=2. Moreover, maybe we can show that F is univalent? Not sure.\n\nLet's think about using the bound on a2 from (e). For a normalized univalent function f(z)=z + a2 z^2 + ..., we have |a2| \u2264 2. How can we relate h to such an f? Since h has a pole at 0, we can consider f(z) = 1/h(z). Then f(0)=0? Let's check: h(z) = 1/z + c0 + c1 z + ... => near 0, h(z) ~ 1/z, so 1/h(z) ~ z. So f(z) = 1/h(z) is holomorphic at 0 with f(0)=0. Moreover, f'(0) = ? Compute: f(z) = 1/h(z) = z / (1 + c0 z + c1 z^2 + ...). Expand: f(z) = z (1 - c0 z + (c0^2 - c1) z^2 + ... ) = z - c0 z^2 + (c0^2 - c1) z^3 + ... . So f'(0)=1. Also f is injective? Since h is injective and nonzero? Actually h is injective and never zero? Does h omit 0? Not necessarily; h may take 0. But if h is injective and has a pole at 0, then h(z)=0 may have at most one solution. However, f(z)=1/h(z) will be injective if h is injective and never zero? Let's check: Suppose f(z1)=f(z2). Then 1/h(z1)=1/h(z2) => h(z1)=h(z2) => z1=z2 by injectivity of h. So f is injective wherever h(z1) and h(z2) are finite and nonzero. However, if h(z)=0 at some point, then f has a pole there? Actually if h(z0)=0, then f(z0) is infinite (pole). But f is supposed to be holomorphic on D? We defined f(z)=1/h(z). Since h is meromorphic with a simple pole at 0, h may have zeros elsewhere. Then f will have poles at those zeros, so f may not be holomorphic on all D. However, we can possibly restrict to a smaller disk where h has no zeros? Not guaranteed.\n\nBut maybe we can choose a rotation or translation to ensure h omits 0? In the application to Koebe theorem, h=1/f omits 0 because f(0)=0 and f injective => f(z)\u22600 for z\u22600, so 1/f omits 0. So in that case, h omits 0. So in (f), we might be able to assume that one of the omitted values is 0? Actually the statement of (f) is general: h omits z1 and z2. But we can apply it to h=1/f which omits 0 and 1/w. So one omitted value is 0. So perhaps we can prove (f) under the assumption that one of the omitted values is 0, and then the general case follows by translation? Let's see: If h omits z1 and z2, then consider H(z) = h(z) - z1. Then H omits 0 and z2 - z1. Moreover, H(z) = 1/z + (c0 - z1) + c1 z + ... . So H is of the same form (simple pole at 0 with residue 1) and omits 0 and some value W = z2 - z1. Then we want to show |W| \u2264 4. So it suffices to prove the lemma under the assumption that one omitted value is 0. Then the general case follows by subtracting z1.\n\nThus we can assume w.l.o.g. that h omits 0 and some value W. Then we want to show |W| \u2264 4.\n\nNow, h omits 0 means h(z) \u2260 0 for all z in D. Since h has a simple pole at 0 with residue 1, near 0 h(z) \u2248 1/z, so it's large, not zero. So omitting 0 is plausible.\n\nNow, define f(z) = 1/h(z). Then f is holomorphic on D? Since h omits 0, h(z) never zero, so f(z) = 1/h(z) is holomorphic on D. Moreover, f(0) = 0 because h(z) ~ 1/z => f(z) ~ z. Compute f'(0) = 1 as before. Also f is injective? Since h is injective and never zero, f(z1)=f(z2) => 1/h(z1)=1/h(z2) => h(z1)=h(z2) => z1=z2. So f is injective. Moreover, f omits the value 1/W? Because h omits W => 1/h omits 1/W? Actually if h(z) \u2260 W for all z, then f(z) = 1/h(z) \u2260 1/W. So f omits 1/W. Also f(0)=0, f'(0)=1. So f is a normalized univalent function omitting the value 1/W. Then by part (e) we have |a2| \u2264 2 for f. But we also can compute a2 in terms of h's coefficients. Let's compute.\n\nGiven h(z) = 1/z + c0 + c1 z + c2 z^2 + ... . Since h omits 0, we can write f(z) = 1/h(z). Expand:\n\nLet h(z) = (1/z) * H(z) where H(z) = 1 + c0 z + c1 z^2 + c2 z^3 + ... . Then f(z) = z / H(z) = z * (1 - c0 z + (c0^2 - c1) z^2 + (-c0^3 + 2c0 c1 - c2) z^3 + ... ). So\n\nf(z) = z - c0 z^2 + (c0^2 - c1) z^3 + ... .\n\nThus f(z) = z + a2 z^2 + a3 z^3 + ... with a2 = -c0.\n\nWait check: coefficient of z^2 is -c0. So a2 = -c0.\n\nNow, f omits the value 1/W. So we can apply the bound on a2 from part (e) to f? Part (e) gave |a2| \u2264 2 for any normalized univalent function. So we get |c0| \u2264 2.\n\nBut we need a bound on W, not on c0. How to get W from c0 and maybe c1? Let's also compute the coefficient a3 maybe related to W.\n\nAlternatively, we can consider the function g(z) = 1/(f(z) - 1/W). Since f omits 1/W, this function is holomorphic, etc. Might lead to bound.\n\nBut perhaps there is a more direct way: Use the area theorem on the function\n\n\u03a6(z) = \\frac{1}{h(z)} + \\frac{1}{h(z) - W}.\n\nSince h omits 0 and W, both denominators never zero. Let's compute its expansion.\n\nWe have 1/h(z) = f(z) = z - c0 z^2 + ... .\n\nAlso 1/(h(z)-W) = ? Let's compute: h(z)-W = 1/z + (c0 - W) + c1 z + ... . Its reciprocal: we can compute similarly: 1/(h(z)-W) = z - (c0 - W) z^2 + ... .\n\nThus\n\n\u03a6(z) = (z - c0 z^2 + ...) + (z - (c0 - W) z^2 + ...) = 2z - (2c0 - W) z^2 + ... .\n\nSo \u03a6(z)/z = 2 - (2c0 - W) z + ... .\n\nNow, consider the function \u03a8(z) = \u03a6(z)/z. It is holomorphic, \u03a8(0)=2. Moreover, maybe we can show that \u03a8 is univalent? Not sure.\n\nAlternatively, consider the function\n\n\u03a9(z) = \\frac{\u03a6(z)}{2} = z - \\frac{2c0 - W}{2} z^2 + ... .\n\nThis is of the form z + A z^2 + ... with A = -(2c0 - W)/2. If we could show that \u03a9 is univalent, then by part (e) we would have |A| \u2264 2, giving |2c0 - W| \u2264 4. Combined with |c0| \u2264 2 from earlier, we could bound |W| \u2264 |2c0| + |2c0 - W| \u2264 4 + 4 = 8, not good.\n\nBut maybe we can show that \u03a9 is univalent without extra assumptions? Let's test: \u03a9(z) = (1/(2h(z)) + 1/(2(h(z)-W))). Not obviously univalent.\n\nLet's step back and think about the known proof of the lemma using area theorem directly on h. Perhaps we can apply area theorem to the function\n\nH(z) = \\frac{1}{h(z)} + \\frac{1}{h(z) - W}.\n\nWe computed its expansion: H(z) = 2z - (2c0 - W) z^2 + ... . So H(z) has a simple zero at 0? Actually leading term 2z, so zero of order 1. Then consider K(z) = H(z)/z = 2 - (2c0 - W) z + ... . This is holomorphic and nonzero at 0 (value 2). Then consider L(z) = 1/K(z) = z/H(z). This has expansion: L(z) = (1/2) z + ...? Actually compute: H(z) = 2z + \u03b1 z^2 + ... where \u03b1 = -(2c0 - W). Then 1/H(z) = (1/(2z)) * 1/(1 + (\u03b1/(2)) z + ...) = (1/(2z)) (1 - (\u03b1/2) z + ...) = 1/(2z) - \u03b1/4 + ... . So L(z) = z/H(z) = 1/2 - (\u03b1/4) z + ... . So L(z) is holomorphic at 0 with value 1/2. Not helpful.\n\nMaybe we should consider the function\n\nM(z) = \\frac{h(z)}{h(z) - W}.\n\nSince h omits 0 and W, this is holomorphic and never 0 or \u221e? Actually numerator never zero (h omits 0), denominator never zero (h omits W). So M is holomorphic and nonzero. Moreover, as z\u21920, h(z) ~ 1/z, so M(z) ~ (1/z)/(1/z) = 1. So M(0)=1. Also M omits 1? Because M(z)=1 would imply h(z) = h(z)-W => W=0, which is false if W\u22600. So M omits 0,1,\u221e. Thus by Picard, M is constant, leading to W=0. So again Picard gives triviality. So we need to avoid Picard.\n\nThus the area theorem approach must give a bound without invoking Picard, and the bound 4 is not sharp for the case where one omitted value is 0? Actually if h omits 0 and W, then the function M(z) = h(z)/(h(z)-W) omits 0,1,\u221e, so by Picard it's constant, forcing W=0. So any non-constant h cannot omit both 0 and another value? Wait that would imply that a meromorphic function on D with a simple pole at 0 cannot omit two values, one of which is 0. But we have examples: h(z) = 1/z + c omits a disk of radius 1 around c, which includes 0 if |c| < 1? Actually if c=0, h(z)=1/z omits 0? No, h(z)=1/z takes all nonzero values, omits 0? As z\u21920, h\u2192\u221e, but 0 is not attained because equation 1/z = 0 has no solution. So h(z)=1/z omits 0. Does it omit another value? It omits no other finite value because for any w \u2260 0, solve 1/z = w => z = 1/w, which is in D if |1/w| < 1 => |w| > 1. So h omits the closed disk |w| \u2264 1? Actually for |w| \u2264 1, the solution z = 1/w has |z| \u2265 1, so not in D (except maybe boundary). So h(z)=1/z omits the closed unit disk. So it omits infinitely many values, including 0 and many others. So h omits 0 and also omits, say, 0.5. So h omits two values (0 and 0.5). Yet h is not constant. So the Picard argument fails because M(z) = h(z)/(h(z)-0.5) is not holomorphic? Let's check: h(z) = 1/z. Then M(z) = (1/z) / (1/z - 0.5) = 1 / (1 - 0.5 z). This is holomorphic on D (since denominator 1 - 0.5 z \u2260 0 for |z|<2). It omits 0? Numerator 1, never zero. It omits \u221e? Denominator never zero. It omits 1? Solve 1/(1-0.5z)=1 => 1 = 1 - 0.5z => z=0. So at z=0, M(0)=1. So M takes the value 1 at z=0. So M does not omit 1; it attains 1 at 0. So the earlier claim that M omits 1 is false: M(z)=1 iff h(z) = h(z)-W => W=0, but we forgot that h(z) may be infinite? Actually solving M(z)=1 gives h(z)/(h(z)-W)=1 => h(z) = h(z)-W => W=0. So if W\u22600, the equation has no solution in C where h(z) is finite. However, if h(z) has a pole, then both numerator and denominator are infinite, and the ratio may be defined as limit. At a pole of h, both numerator and denominator have a pole; the ratio may tend to 1. Indeed, at z=0, h has a pole, so we need to evaluate limit: lim_{z\u21920} h(z)/(h(z)-W) = lim (1/z + ...)/(1/z + ... - W) = 1. So M(z) can equal 1 at the pole (by continuous extension). So M omits 0 and \u221e, but may attain 1. So M omits only two values (0 and \u221e), not three. So Picard's theorem for holomorphic functions (which requires omitting three values) does not apply because M is holomorphic and omits only 0 and \u221e (i.e., never 0 and never \u221e). Actually omitting \u221e means it's bounded? No, a holomorphic function on D can omit \u221e trivially because \u221e is not a value in C; the condition of omitting \u221e is vacuous for holomorphic functions. So Picard's little theorem says a holomorphic function from D to C omitting two values is constant. Here M omits 0 only? Wait M never equals 0 because numerator never zero. Does M ever equal \u221e? No, as a holomorphic function, it never equals \u221e. So M omits 0 and \u221e? But omitting \u221e is not a restriction because the codomain is C; \u221e is not in C. So the condition is just that M never takes the value 0. So M omits only one value (0). Thus Picard does not force constancy. So the earlier attempt to use Picard incorrectly assumed that omitting \u221e is a condition, but it's not for holomorphic functions. So we need a different approach.\n\nThus we need to prove (f) using area theorem, likely by considering the function\n\n\u03c6(z) = \\frac{1}{h(z)} + \\frac{1}{h(z) - W}\n\nand applying part (c) to something like its reciprocal or derivative.\n\nLet's try to derive a bound on W from the coefficients we have.\n\nWe have h(z) = 1/z + c0 + c1 z + c2 z^2 + ... . Since h omits 0 and W, we know that h(z) \u2260 0 and h(z) \u2260 W for all z.\n\nDefine\n\nA(z) = \\frac{1}{h(z)} = f(z) (as before). Then f is holomorphic, f(0)=0, f'(0)=1, f omits 1/W.\n\nDefine\n\nB(z) = \\frac{1}{h(z) - W}. Then B is holomorphic, B(0)=0? Let's check: As z\u21920, h(z) ~ 1/z, so h(z)-W ~ 1/z, so B(z) ~ z. So B(0)=0. Also B'(0)=1? Compute: B(z) = 1/(h(z)-W) = z / (1 + (c0 - W)z + c1 z^2 + ...). Expand: B(z) = z (1 - (c0 - W)z + ...) = z - (c0 - W) z^2 + ... . So B'(0)=1. Also B is injective? Since h is injective and omits W, h(z1)-W = h(z2)-W => h(z1)=h(z2) => z1=z2. So B is injective. Moreover, B omits the value -W/(??) Actually B omits? Since h omits W, B never has pole? Actually B is holomorphic; does B omit any value? B(z) = 0 only if h(z)-W has a pole, i.e., h(z) has a pole, which only occurs at z=0. At z=0, B(0)=0. So B attains 0 only at z=0. So B omits no nonzero value? Not sure.\n\nBut we have two normalized univalent functions f and B, both with f(0)=B(0)=0, f'(0)=B'(0)=1. Their coefficients: f(z) = z - c0 z^2 + (c0^2 - c1) z^3 + ... ; B(z) = z - (c0 - W) z^2 + ... .\n\nThus the coefficient of z^2 in f is a2 = -c0; in B is b2 = -(c0 - W) = -c0 + W.\n\nNow, by part (e), we know that for any normalized univalent function, |a2| \u2264 2 and |b2| \u2264 2. So we have\n\n|c0| \u2264 2,\n| -c0 + W | \u2264 2.\n\nThus |W| = |(-c0 + W) + c0| \u2264 | -c0 + W| + |c0| \u2264 2 + 2 = 4.\n\nThus |W| \u2264 4. This proves (f) under the assumption that h omits 0 and W. Then the general case follows by translation: if h omits z1 and z2, then H(z) = h(z) - z1 omits 0 and W = z2 - z1, and H is of the same form (simple pole at 0 with residue 1). Applying the above yields |z2 - z1| \u2264 4.\n\nThus (f) is proved using (e) and the construction of f and B as reciprocals of h and h-W. This matches the hint: \"Look at the second coefficient in the power series expansion of 1/(h(z) - z_j).\" Indeed, 1/(h(z)-z_j) is B_j(z) (up to maybe a factor). Its expansion gives the coefficient of z^2 as -(c0 - z_j). Then applying part (e) to the function 1/(h(z)-z_j) (which is normalized univalent) yields bound on that coefficient, leading to bound on difference.\n\nThus we have a clear path for (f). Let's flesh out details:\n\n- Show that if h omits z1 and z2, then for each j, the function f_j(z) = 1/(h(z)-z_j) is holomorphic on D, satisfies f_j(0)=0, f_j'(0)=1, and is injective (since h is injective and omits z_j). Then apply part (e) to f_j to get |a_{2}^{(j)}| \u2264 2, where a_{2}^{(j)} is the coefficient of z^2 in f_j's expansion.\n\n- Compute the expansion: f_j(z) = z - (c0 - z_j) z^2 + O(z^3). So a_{2}^{(j)} = -(c0 - z_j).\n\n- Hence |c0 - z_j| \u2264 2 for j=1,2.\n\n- Then by triangle inequality, |z1 - z2| = |(c0 - z2) - (c0 - z1)| \u2264 |c0 - z2| + |c0 - z1| \u2264 2 + 2 = 4.\n\nThus (f) proved.\n\nNow we need to ensure that f_j is indeed injective: h is injective and omits z_j, so h(z1)-z_j = h(z2)-z_j implies h(z1)=h(z2) implies z1=z2. So f_j is injective.\n\nAlso need to check that f_j is holomorphic on D: Since h omits z_j, denominator never zero, so f_j is holomorphic. At z=0, h has a pole, so h(z)-z_j also has a pole, but its reciprocal has a removable zero? Actually as we computed, f_j(z) = z * (something holomorphic and nonzero at 0), so f_j is holomorphic at 0 with f_j(0)=0.\n\nNow we need to verify f_j'(0)=1. Compute derivative: f_j(z) = 1/(h(z)-z_j). Write h(z) = 1/z + \u03c6(z) where \u03c6(z) = c0 + c1 z + c2 z^2 + ... . Then h(z)-z_j = 1/z + (c0 - z_j) + \u03c6(z) - c0? Actually \u03c6(z) already includes c0, so h(z)-z_j = 1/z + (c0 - z_j) + c1 z + c2 z^2 + ... . Then f_j(z) = z / [1 + (c0 - z_j) z + c1 z^2 + c2 z^3 + ...] = z * [1 - (c0 - z_j) z + ((c0 - z_j)^2 - c1) z^2 + ...]. So f_j(z) = z - (c0 - z_j) z^2 + ... . So f_j'(0)=1.\n\nThus part (e) applies.\n\nNow part (e) itself: We need to prove |a2| \u2264 2 for normalized univalent f(z)=z + a2 z^2 + ... . The solution sketch used part (d) and (c). Let's verify that proof.\n\nPart (d): Given f normalized univalent, show there exists g normalized univalent such that g^2(z) = f(z^2). Construction: Since f(z)/z is nowhere zero and holomorphic on D, we can define a holomorphic square root \u03c8 with \u03c8(0)=1. Then set g(z) = z \u03c8(z^2). Show g is injective, g(0)=0, g'(0)=1, and g^2(z) = f(z^2). Need to verify injectivity: Suppose g(z1)=g(z2). Then z1 \u03c8(z1^2) = z2 \u03c8(z2^2). Square both sides: z1^2 \u03c8(z1^2)^2 = z2^2 \u03c8(z2^2)^2 => f(z1^2) = f(z2^2). Since f is injective, z1^2 = z2^2. So z1 = \u00b1 z2. But g is odd? Let's check: g(-z) = (-z) \u03c8((-z)^2) = -z \u03c8(z^2) = -g(z). So g is odd. Thus if z1 = -z2, then g(z1) = -g(z2). For them to be equal, we need g(z1)=g(z2) => -g(z2)=g(z2) => g(z2)=0 => z2=0 => z1=0. So the only case is z1=z2=0. Hence injective.\n\nThus (d) is solid.\n\nPart (e): Using g, we compute 1/g(z) expansion and apply (c) to get bound on a2.\n\nLet's detail:\n\nFrom (d), g(z) = z \u03c8(z^2) where \u03c8^2(z) = f(z)/z, \u03c8(0)=1.\n\nSince f(z) = z + a2 z^2 + a3 z^3 + ... , we have f(z)/z = 1 + a2 z + a3 z^2 + ... . So \u03c8(z) = sqrt{1 + a2 z + a3 z^2 + ... } = 1 + (a2/2) z + ... . So \u03c8(z^2) = 1 + (a2/2) z^2 + ... . Then g(z) = z (1 + (a2/2) z^2 + ... ) = z + (a2/2) z^3 + ... . So g is odd: only odd powers.\n\nThus 1/g(z) = 1/z * 1/(1 + (a2/2) z^2 + ... ) = 1/z * (1 - (a2/2) z^2 + ... ) = 1/z - (a2/2) z + ... .\n\nSo 1/g(z) = 1/z + b0 + b1 z + b2 z^2 + ... with b1 = -a2/2 (coefficient of z). All other b_n for even n? Actually expansion: 1/g(z) = 1/z + b0 + b1 z + b2 z^2 + ... . Since g is odd, 1/g is odd? Let's check: g(-z) = -g(z) => 1/g(-z) = -1/g(z). So 1/g is odd as well. So its expansion contains only odd powers: 1/g(z) = 1/z + b1 z + b3 z^3 + ... . So b0 = 0, b2 = 0, etc. So b1 is the coefficient of z.\n\nThus by part (c) applied to 1/g(z) (which is of the form 1/z + c0 + c1 z + ... injective on punctured disc), we have sum_{n>=1} n|b_n|^2 \u2264 1. In particular, the n=1 term gives 1*|b1|^2 \u2264 1 => |b1| \u2264 1. Hence |a2/2| \u2264 1 => |a2| \u2264 2.\n\nEquality case: If |a2|=2, then |b1|=1, and equality in the area theorem forces 1/g(z) to have the form 1/z + e^{i\u03b8} z (i.e., only b1 nonzero). Then we can solve for g and f as in the sketch.\n\nThus (e) is proved.\n\nNow (c): Prove area theorem bound.\n\nWe need to show: If h(z) = 1/z + c0 + c1 z + c2 z^2 + ... is injective on 0<|z|<1, then sum_{n>=1} n|c_n|^2 \u2264 1.\n\nProof: For 0<\u03c1<1, consider the image of the annulus? Actually we consider the image of the punctured disk D_\u03c1\\{0} under h. Since h is injective, the area of h(D_\u03c1\\{0}) can be computed via the Jacobian: area = \u222b_{D_\u03c1\\{0}} |h'(z)|^2 dA(z). Alternatively, we can compute the area of the complement of h(D_\u03c1\\{0}) in the extended complex plane? The area theorem usually considers the complement of the image of a univalent function on the exterior of the unit disk. But here we have a punctured disk. However, we can apply a change of variable w = 1/z to map the punctured disk to the exterior of the unit disk. Let's do that.\n\nDefine H(w) = h(1/w). Then for |w|>1, H(w) is analytic? Let's see: h(z) = 1/z + c0 + c1 z + c2 z^2 + ... . Then h(1/w) = w + c0 + c1/w + c2/w^2 + ... . So H(w) = w + c0 + c1/w + c2/w^2 + ... for |w|>1. This is analytic on |w|>1 (the exterior of the unit disk) and has a simple pole at infinity? Actually as w\u2192\u221e, H(w) ~ w + c0 + ... . So H(w) is univalent on |w|>1? Since h is injective on 0<|z|<1, the map w\u21921/w is a bijection between {|w|>1} and {0<|z|<1}. So H is injective on |w|>1. Moreover, H has a simple pole at w=\u221e? Actually as w\u2192\u221e, H(w) ~ w, so it has a simple pole at infinity with residue 1. The area theorem for functions univalent on the exterior of the unit disk with expansion F(w) = w + b0 + b1/w + b2/w^2 + ... says that sum_{n>=1} n|b_n|^2 \u2264 1. This is a standard result (Gronwall's area theorem). Here our H(w) = w + c0 + c1/w + c2/w^2 + ... . So the coefficients b_n = c_n. Then the area theorem gives sum_{n>=1} n|c_n|^2 \u2264 1. This is exactly what we need.\n\nThus we can prove (c) by mapping to the exterior and applying the known area theorem. Or we can directly compute area of complement of h(D_\u03c1\\{0}) and let \u03c1\u21921.\n\nLet's produce a direct proof: For 0<\u03c1<1, consider the image of the circle |z|=\u03c1 under h. Since h is injective, the curve h(|z|=\u03c1) is a simple closed curve. The area enclosed by this curve can be computed via Green's formula: Area = (1/2i) \u222b_{|z|=\u03c1} \\overline{h(z)} h'(z) dz. Expand h(z) and h'(z) in series, integrate term by term, get area = \u03c0(1/\u03c1^2 - sum_{n>=1} n|c_n|^2 \u03c1^{2n}). Since the area is nonnegative, we get the inequality. Then let \u03c1\u21921^- to get sum n|c_n|^2 \u2264 1.\n\nWe'll present that.\n\nNow (a) and (b) are straightforward.\n\nFinally (g): Complete the proof: Suppose f is normalized univalent and omits w \u2260 0. Then consider h(z) = 1/f(z). Show h is of the form 1/z + ... and omits 0 and 1/w. Apply (f) to get |1/w| \u2264 4 => |w| \u2265 1/4. Show that 1/4 is attained by the Koebe function k(z) = z/(1-z)^2, which omits -1/4. Hence the best possible radius is 1/4.\n\nNow we need to write a full solution with proofs for each part, showing all reasoning.\n\nLet's structure the answer:\n\n- Introduction: restate problem.\n\n- Part (a): Provide counterexample f_n(z)=z/n. Show f_n(0)=0, holomorphic, f_n'(0)=1/n, image is D_{1/n}(0), so 1/n not in image. Conclude no uniform r.\n\n- Part (b): Provide f_\u03b5(z)=\u03b5(e^{z/\u03b5}-1). Show f_\u03b5(0)=0, f_\u03b5'(0)=1, image omits -\u03b5. Conclude no uniform r.\n\n- Part (c): Prove area theorem bound.\n\n   * Let h(z)=1/z + c0 + c1 z + ... be injective on 0<|z|<1.\n   * For 0<\u03c1<1, consider the curve \u03b3_\u03c1(t)=h(\u03c1 e^{it}), t\u2208[0,2\u03c0]. Since h is injective, \u03b3_\u03c1 is a simple closed curve.\n   * Compute area A(\u03c1) enclosed by \u03b3_\u03c1 using Green's theorem: A(\u03c1) = (1/2i) \u222e_{\u03b3_\u03c1} \\overline{w} dw = (1/2i) \u222e_{|z|=\u03c1} \\overline{h(z)} h'(z) dz.\n   * Insert series: h(z)=z^{-1}+\u2211_{k\u22650} c_k z^k, h'(z)=-z^{-2}+\u2211_{k\u22650} (k+1) c_{k+1} z^k.\n   * Compute product and integrate termwise; only terms where powers of z cancel give nonzero contribution.\n   * Obtain A(\u03c1)=\u03c0(\u03c1^{-2} - \u2211_{n\u22651} n|c_n|^2 \u03c1^{2n}).\n   * Since area \u22650, we have \u2211 n|c_n|^2 \u03c1^{2n} \u2264 \u03c1^{-2} for all \u03c1<1.\n   * Let \u03c1\u21921^\u2212 to get \u2211 n|c_n|^2 \u2264 1.\n\n- Part (d): Given f(z)=z + a2 z^2 + ... injective, f(0)=0, f'(0)=1.\n\n   * Show f(z)/z is nowhere zero on D and holomorphic, with value 1 at 0.\n   * Define \u03c8(z) a holomorphic square root of f(z)/z with \u03c8(0)=1 (exists because D is simply connected and f(z)/z \u22600).\n   * Set g(z)=z \u03c8(z^2). Then g(0)=0, g'(0)=\u03c8(0)=1.\n   * Show g^2(z)=z^2 \u03c8(z^2)^2 = z^2\u00b7(f(z^2)/z^2)=f(z^2).\n   * Prove g is injective: Suppose g(z1)=g(z2). Then squaring gives f(z1^2)=f(z2^2) \u21d2 z1^2=z2^2 \u21d2 z1=\u00b1z2. If z1=-z2\u22600, then g(z1)=-g(z2)\u2260g(z2) unless g(z2)=0 \u21d2 z2=0 \u21d2 z1=0. Hence z1=z2.\n   * Thus g satisfies the hypotheses.\n\n- Part (e): Bound on a2.\n\n   * From (d), g(z)=z + (a2/2) z^3 + ... (only odd powers).\n   * Hence 1/g(z)=1/z - (a2/2) z + ... .\n   * Write 1/g(z)=1/z + b0 + b1 z + b2 z^2 + ... . By oddness, b0=b2=...=0, b1=-a2/2.\n   * Since g satisfies the hypotheses of the theorem, 1/g is of the form 1/z + c0 + c1 z + ... injective on 0<|z|<1 (simple pole at 0, residue 1). Apply part (c): \u2211 n|b_n|^2 \u2264 1 \u21d2 |b1|^2 \u2264 1 \u21d2 |a2|/2 \u2264 1 \u21d2 |a2| \u2264 2.\n   * Equality: If |a2|=2, then |b1|=1 and equality in (c) forces 1/g(z)=1/z + e^{i\u03b8} z for some \u03b8\u2208\u211d (all higher coefficients zero). Solving gives g(z)=z/(1+e^{i\u03b8}z^2). Then f(z^2)=g(z)^2 = z^2/(1+e^{i\u03b8}z^2)^2 \u21d2 f(z)=z/(1+e^{i\u03b8}z)^2. Conversely, these functions satisfy the hypotheses and give |a2|=2.\n\n- Part (f): Bound on distance between two omitted values.\n\n   * Let h(z)=1/z + c0 + c1 z + ... be injective on D and omit two distinct values z1, z2.\n   * Define for j=1,2 the functions f_j(z)=1/(h(z)-z_j). Since h omits z_j, f_j is holomorphic on D. Moreover, f_j(0)=0, f_j'(0)=1, and f_j is injective (because h is injective).\n   * Thus f_j satisfies the hypotheses of the theorem. By part (e), the coefficient of z^2 in f_j's expansion, call it a_2^{(j)}, satisfies |a_2^{(j)}| \u2264 2.\n   * Compute the expansion: h(z)-z_j = 1/z + (c0-z_j) + c1 z + c2 z^2 + ... . Hence\n        f_j(z) = 1/(h(z)-z_j) = z - (c0-z_j) z^2 + O(z^3).\n     So a_2^{(j)} = -(c0-z_j).\n   * Therefore |c0 - z_j| \u2264 2 for j=1,2.\n   * By the triangle inequality,\n        |z1 - z2| = |(c0 - z2) - (c0 - z1)| \u2264 |c0 - z2| + |c0 - z1| \u2264 2 + 2 = 4.\n   * Hence |z1 - z2| \u2264 4.\n\n- Part (g): Koebe\u2013Bieberbach radius theorem.\n\n   * Let f be injective on D with f(0)=0, f'(0)=1. Suppose there exists w\u2208\u2102 with |w|<1/4 such that w\u2209f(D). We'll derive a contradiction.\n   * Since f is injective and f(0)=0, we have f(z)\u22600 for z\u22600. Hence the function h(z)=1/f(z) is holomorphic on D.\n   * Moreover, h has a simple pole at 0 with residue 1 because f(z)=z+\u22ef \u21d2 h(z)=1/z+\u22ef. So h(z)=1/z + c0 + c1 z + \u22ef.\n   * Since w\u2209f(D), we have f(z)\u2260w for all z\u2208D. Hence h(z)\u22601/w for all z\u2208D. Also h(z)\u22600 because f(z)\u2260\u221e (f is holomorphic) and f(z)=0 only at z=0, but h has a pole at 0, so h(z)\u22600 for z\u22600; at z=0, h has a pole, so we consider the punctured disk: h omits 0 on D\\{0}. Thus h omits the two values 0 and 1/w on D\\{0}.\n   * Apply part (f) to h (which is injective on D\\{0} and of the required form) to obtain |0 - 1/w| \u2264 4, i.e., |1/w| \u2264 4 \u21d2 |w| \u2265 1/4.\n   * This contradicts |w|<1/4. Therefore every w with |w|<1/4 belongs to f(D). Hence D_{1/4}(0) \u2286 f(D).\n   * To see that 1/4 is best possible, consider the Koebe function k(z)=z/(1-z)^2. It satisfies k(0)=0, k'(0)=1, is injective on D, and its image is \u2102 \\ (\u2212\u221e,\u22121/4]. In particular, \u22121/4\u2209k(D), so no larger radius works.\n   * Thus the best possible constant is r=1/4.\n\n- Conclude Q.E.D.\n\nWe need to ensure all steps are rigorous, especially the injectivity of h on D\\{0} in part (g). Since f is injective on D and f(0)=0, for z1\u2260z2 in D\\{0}, if f(z1)=f(z2) then z1=z2 by injectivity. So f is injective on D\\{0} as well. Then h=1/f is also injective on D\\{0} because if 1/f(z1)=1/f(z2) then f(z1)=f(z2) \u21d2 z1=z2. Also h never takes the value 0 on D\\{0} because f(z)\u22600 for z\u22600. So h omits 0 on D\\{0}. Also h omits 1/w because f(z)\u2260w \u21d2 h(z)\u22601/w. So h omits two values on D\\{0}. However, part (f) required h to be defined and injective on the whole D (including 0?) Actually the statement of (f) says: \"If h(z) = 1/z + c0 + c1 z + ... is injective on D and avoids the values z1 and z2, show that |z1 - z2| \u2264 4.\" It assumes h is defined on D (i.e., holomorphic on D) with that Laurent expansion (so it has a simple pole at 0). In our case, h has a simple pole at 0, so it's not holomorphic at 0 but meromorphic. However, the expansion shows it's of the form 1/z + ... . The condition \"injective on D\" likely means injective as a map from D to the Riemann sphere, allowing the pole at 0 to map to \u221e. Usually, for such meromorphic functions, injective means that if z1\u2260z2 then h(z1)\u2260h(z2) (including the case where one or both equal \u221e). Since h has a simple pole at 0, h(0)=\u221e. For any other z\u22600, h(z) is finite, so h(z)\u2260\u221e. Thus injectivity holds if h is injective on D\\{0} and h(0)=\u221e is not attained elsewhere. Since f omits 0, h(z)=1/f(z) never equals 0, so h(z)\u2260\u221e? Wait h(z)=\u221e only when f(z)=0, which only occurs at z=0. So h(0)=\u221e, and for z\u22600, h(z) is finite. So h is injective on D as a map to the Riemann sphere. So the hypothesis of (f) is satisfied: h is meromorphic on D with a simple pole at 0, injective, and has the expansion 1/z + c0 + c1 z + ... . It omits the values 0 and 1/w (since h(z) never equals 0 nor 1/w). So we can apply (f) directly.\n\nThus part (g) works.\n\nNow we need to write the solution in a clear, step-by-step manner, with full proofs.\n\nLet's produce the final answer.\n\n",
    "format": "unknown",
    "index": 0
  }
]
```

---

## Raw Response (truncated)

```json
{
  "id": "gen-1789209008-FfYSBggzWW4OTqhhMnSq",
  "object": "chat.completion",
  "created": 1789209008,
  "model": "nvidia/nemotron-3-super-120b-a12b:free",
  "provider": "Nvidia",
  "system_fingerprint": null,
  "service_tier": null,
  "choices": [
    {
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop",
      "native_finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "**Solution**\n\nLet \\(\\mathbb D=\\{z\\in\\mathbb C:|z|<1\\}\\).  \nA function \\(f:\\mathbb D\\to\\mathbb C\\) is *normalized* if \\(f(0)=0\\) and \\(f'(0)=1\\).\n\n--------------------------------------------------------------------\n### (a)  No uniform radius without further hypotheses\n\nFor \\(n\\in\\mathbb N\\) set  \n\n\\[\nf_n(z)=\\frac{z}{n},\\qquad z\\in\\mathbb D .\n\\]\n\n* \\(f_n(0)=0\\) and \\(f_n\\) is holomorphic on \\(\\mathbb D\\).\n* \\(f_n' (z)=\\frac1n\\), hence \\(f_n'(0)=\\frac1n\\).\n* \\(f_n(\\mathbb D)=\\{w:|w|<\\frac1n\\}=D_{1/n}(0)\\); therefore \\(\\frac1n\\notin f_n(\\mathbb D)\\).\n\nIf a number \\(r>0\\) worked for every such \\(f\\), then for any \\(n\\) we would have  \n\\(D_r(0)\\subset f_n(\\mathbb D)\\).  Choosing \\(n\\) with \\(\\frac1n<r\\) gives  \n\\(\\frac1n\\in D_r(0)\\) but \\(\\frac1n\\notin f_n(\\mathbb D)\\), a contradiction.  \nHence no such \\(r\\) exists.\n\n--------------------------------------------------------------------\n### (b)  The hypothesis \\(f'(0)=1\\) still does not give a uniform radius\n\nFor \\(\\varepsilon>0\\) define  \n\n\\[\nf_\\varepsilon(z)=\\varepsilon\\bigl(e^{z/\\varepsilon}-1\\bigr),\\qquad z\\in\\mathbb D .\n\\]\n\n* \\(f_\\varepsilon(0)=0\\) and  \n  \\(f_\\varepsilon'(z)=e^{z/\\varepsilon}\\), so \\(f_\\varepsilon'(0)=1\\).\n* Since \\(e^{z/\\varepsilon}\\neq0\\) for all \\(z\\), we have  \n  \\(f_\\varepsilon(z)\\neq-\\varepsilon\\) for every \\(z\\in\\mathbb D\\); thus \\(-\\varepsilon\\notin f_\\varepsilon(\\mathbb D)\\).\n\nIf a radius \\(r>0\\) worked for all such functions, then for any \\(\\varepsilon<r\\) we would have  \n\\(-\\varepsilon\\in D_r(0)\\) but \\(-\\varepsilon\\notin f_\\varepsilon(\\mathbb D)\\), impossible.  \nHence no uniform radius exists even after imposing \\(f'(0)=1\\).\n\n--------------------------------------------------------------------\n### (c)  Area theorem for a function with a simple pole\n\nLet  \n\n\\[\nh(z)=\\frac1z+c_0+c_1z+c_2z^2+\\cdots\n\\]\n\nbe injective on the punctured disc \\(0<|z|<1\\).  \nFor \\(0<\\rho<1\\) consider the curve  \n\n\\[\n\\gamma_\\rho(t)=h(\\rho e^{it}),\\qquad 0\\le t\\le2\\pi .\n\\]\n\nBecause \\(h\\) is injective, \\(\\gamma_\\rho\\) is a simple closed curve; let \\(A(\\rho)\\) be the area of its interior.  \nBy Green\u2019s theorem,\n\n\\[\nA(\\rho)=\\frac1{2i}\\oint_{\\gamma_\\rho}\\overline w\\,dw\n      =\\frac1{2i}\\oint_{|z|=\\rho}\\overline{h(z)}\\,h'(z)\\,dz .\n\\]\n\nWrite the Laurent expansions\n\n\\[\nh(z)=z^{-1}+\\sum_{k\\ge0}c_kz^k,\\qquad\nh'(z)=-z^{-2}+\\sum_{k\\ge0}(k+1)c_{k+1}z^k .\n\\]\n\nThen\n\n\\[\n\\overline{h(z)}\\,h'(z)\n =\\bigl(z^{-1}+\\sum_{k\\ge0}\\overline{c_k}\\,\\overline{z}^{\\,k}\\bigr)\n   \\bigl(-z^{-2}+\\sum_{j\\ge0}(j+1)c_{j+1}z^{j}\\bigr) .\n\\]\n\nOn the circle \\(|z|=\\rho\\) we have \\(\\overline{z}=\\rho^{2}/z\\).  \nMultiplying out and integrating termwise, only the terms where the total power of \\(z\\) is \\(-1\\) survive.  \nA short computation gives\n\n\\[\n\\frac1{2i}\\oint_{|z|=\\rho}\\overline{h(z)}\\,h'(z)\\,dz\n   =\\pi\\Bigl(\\rho^{-2}-\\sum_{n\\ge1}n|c_n|^{2}\\rho^{2n}\\Bigr).\n\\]\n\nSince \\(A(\\rho)\\ge0\\),\n\n\\[\n\\sum_{n\\ge1}n|c_n|^{2}\\rho^{2n}\\le\\rho^{-2}\\qquad(0<\\rho<1).\n\\]\n\nLetting \\(\\rho\\to1^{-}\\) (the left\u2013hand side increases with \\(\\rho\\)) yields\n\n\\[\n\\boxed{\\displaystyle\\sum_{n\\ge1}n|c_n|^{2}\\le1}.\n\\]\n\n--------------------------------------------------------------------\n### (d)  Constructing a square\u2011root function\n\nLet  \n\n\\[\nf(z)=z+a_2z^2+a_3z^3+\\cdots\n\\]\n\nbe injective on \\(\\mathbb D\\) with \\(f(0)=0,\\;f'(0)=1\\).\n\nBecause \\(f(z)/z=1+a_2z+a_3z^2+\\cdots\\) is holomorphic and nowhere zero on \\(\\mathbb D\\) (its value at \\(0\\) is \\(1\\)), the simply connected domain \\(\\mathbb D\\) admits a holomorphic square root.  \nChoose \\(\\psi:\\mathbb D\\to\\mathbb C\\) holomorphic with  \n\n\\[\n\\psi^{2}(z)=\\frac{f(z)}{z},\\qquad \\psi(0)=1 .\n\\]\n\nDefine  \n\n\\[\ng(z)=z\\,\\psi(z^{2}),\\qquad z\\in\\mathbb D .\n\\]\n\n* \\(g(0)=0\\) and \\(g'(0)=\\psi(0)=1\\).\n* Moreover,\n  \\[\n  g^{2}(z)=z^{2}\\psi(z^{2})^{2}=z^{2}\\cdot\\frac{f(z^{2})}{z^{2}}=f(z^{2}).\n  \\]\n\n*Injectivity of \\(g\\).*  \nIf \\(g(z_{1})=g(z_{2})\\) then squaring gives \\(f(z_{1}^{2})=f(z_{2}^{2})\\); injectivity of \\(f\\) implies \\(z_{1}^{2}=z_{2}^{2}\\), i.e. \\(z_{1}= \\pm z_{2}\\).  \nIf \\(z_{1}=-z_{2}\\neq0\\) then, using the oddness of \\(g\\) (which follows from \\(g(-z)=-z\\psi((-z)^{2})=-z\\psi(z^{2})=-g(z)\\)), we obtain \\(g(z_{1})=-g(z_{2})\\).  Hence \\(g(z_{1})=g(z_{2})\\) forces \\(g(z_{2})=0\\), which happens only at \\(z_{2}=0\\); consequently \\(z_{1}=z_{2}=0\\).  \nThus \\(g\\) is injective.\n\nTherefore \\(g\\) satisfies the same hypotheses as \\(f\\).\n\n--------------------------------------------------------------------\n### (e)  The bound \\(|a_{2}|\\le2\\) and the extremal functions\n\nFrom the construction in (d),\n\n\\[\n\\psi(z)=1+\\frac{a_{2}}{2}z+\\cdots\\quad\\Longrightarrow\\quad\n\\psi(z^{2})=1+\\frac{a_{2}}{2}z^{2}+\\cdots .\n\\]\n\nHence  \n\n\\[\ng(z)=z\\psi(z^{2})=z+\\frac{a_{2}}{2}z^{3}+\\cdots ,\n\\]\n\nso \\(g\\) contains only odd powers of \\(z\\).  Consequently  \n\n\\[\n\\frac1{g(z)}=\\frac1z\\Bigl(1-\\frac{a_{2}}{2}z^{2}+\\cdots\\Bigr)\n           =\\frac1z-\\frac{a_{2}}{2}z+\\cdots .\n\\]\n\nWrite  \n\n\\[\n\\frac1{g(z)}=\\frac1z+b_{0}+b_{1}z+b_{2}z^{2}+\\cdots .\n\\]\n\nBecause \\(g\\) is odd, \\(1/g\\) is also odd; thus \\(b_{0}=b_{2}=b_{4}=\\cdots=0\\) and  \n\\(b_{1}=-\\dfrac{a_{2}}{2}\\).\n\nThe function \\(1/g\\) is of the form required in part (c): it has a simple pole at \\(0\\) with residue \\(1\\) and is injective on \\(0<|z|<1\\) (injectivity follows from that of \\(g\\)).  \nApplying part (c) to \\(1/g\\) gives  \n\n\\[\n\\sum_{n\\ge1}n|b_{n}|^{2}\\le1\\quad\\Longrightarrow\\quad|b_{1}|^{2}\\le1 .\n\\]\n\nHence  \n\n\\[\n\\Bigl|\\frac{a_{2}}{2}\\Bigr|^{2}\\le1\\quad\\Longrightarrow\\quad|a_{2}|\\le2 .\n\\]\n\n*Equality case.*  \nIf \\(|a_{2}|=2\\) then \\(|b_{1}|=1\\) and equality in the area theorem forces  \n\n\\[\n\\frac1{g(z)}=\\frac1z+e^{i\\theta}z\\qquad(\\theta\\in\\mathbb R)\n\\]\n\n(all higher coefficients vanish).  Solving for \\(g\\),\n\n\\[\ng(z)=\\frac{z}{1+e^{i\\theta}z^{2}} .\n\\]\n\nNow \\(f(z^{2})=g(z)^{2}=\\dfrac{z^{2}}{(1+e^{i\\theta}z^{2})^{2}}\\); replacing \\(z^{2}\\) by \\(z\\) yields  \n\n\\[\nf(z)=\\frac{z}{(1+e^{i\\theta}z)^{2}} .\n\\]\n\nConversely, each function of this form is injective on \\(\\mathbb D\\), satisfies \\(f(0)=0,\\;f'(0)=1\\) and has \\(a_{2}= -2e^{i\\theta}\\), so \\(|a_{2}|=2\\).  \nThus the estimate is sharp.\n\n--------------------------------------------------------------------\n### (f)  Distance between two omitted values\n\nLet  \n\n\\[\nh(z)=\\frac1z+c_{0}+c_{1}z+c_{2}z^{2}+\\cdots\n\\]\n\nbe injective on \\(\\mathbb D\\) and suppose that it omits two (distinct) values \\(z_{1},z_{2}\\).  \nFor \\(j=1,2\\) set  \n\n\\[\nf_{j}(z)=\\frac{1}{h(z)-z_{j}} .\n\\]\n\nBecause \\(h\\) never equals \\(z_{j}\\), each \\(f_{j}\\) is holomorphic on \\(\\mathbb D\\).  \nMoreover,\n\n* \\(f_{j}(0)=0\\) (since \\(h(z)\\sim1/z\\) near \\(0\\)),\n* \\(f_{j}'(0)=1\\) (a direct computation from the expansion below),\n* \\(f_{j}\\) is injective: if \\(f_{j}(z_{1})=f_{j}(z_{2})\\) then  \n  \\(h(z_{1})-z_{j}=h(z_{2})-z_{j}\\) \\(\\Rightarrow\\) \\(h(z_{1})=h(z_{2})\\) \\(\\Rightarrow\\) \\(z_{1}=z_{2}\\) by injectivity of \\(h\\).\n\nThus each \\(f_{j}\\) satisfies the hypotheses of the 
```
