# Studio Design Workflows and Creative Priorities

Research date: 2026-09-30. Status: research and proposed agent adaptation, not an approved implementation plan.

## Selection and Evidence Boundaries

Use rankings to discover cases, not to establish a universal studio hierarchy or infer internal processes. GQ's page dated July 22, 2026 explicitly retains its 2023 poll; 300 people were invited, not necessarily 300 respondents. Useful entries include Breath of the Wild (#1), The Last of Us (#2), Bloodborne (#4), Portal 2 (#8), Half-Life 2 (#10), and Hades (#38). [S1]

BAFTA's April 3, 2025 influence poll was public voting, with Shenmue first, not a jury finding about studio design quality. It supplies a contrasting community signal, not a reason to copy a winning game's process. [S2]

The six cases below are a deliberately varied research shortlist, not those polls' top six studios. Larian supplements the ranking-led selection because its public production retrospective provides a useful systems/iteration contrast. Evidence applies to named projects and periods, not every game or the companies' current confidential practices. Creator accounts are selective retrospectives, not causal proof that a method guarantees success. Supergiant also supplies a smaller-studio counterpoint to the user's large-company framing.

## Case Studies

### Nintendo: Tears of the Kingdom

**Documented:** The developers prioritize supporting expected player actions, welcome unforeseen constructions, and visually mark exceptions: objects deliberately fixed in place receive readable cues. They describe watching player reactions and valuing personally discovered solutions. [S3]

**Flavor inference:** curiosity and the satisfaction of making an idea work.

**Agent proposal:** start from a player intention, prototype a small interaction, test plausible unprompted uses, and specify readable exceptions. Ask what players will want to try before enumerating features.

**Transfer risk:** supporting combinations costs engineering and verification effort. Borrow the principle in one small scene, not the open-world production scale.

### Valve: Half-Life 2

**Documented:** The published deck treats designs as hypotheses, uses unassisted external playtests, recommends rough short slices, and lets observations prioritize subsequent increments. It asks both whether players receive the intended experience and whether that experience is desirable. [S4]

**Flavor inference:** readable, deliberately paced experiences developed through observation rather than internal confidence.

**Agent proposal:** specify intended experience, observable signals, smallest experiment, and continue/revise/stop criteria before building. Separate a playtest from assisted teaching and from rule tests.

**Transfer risk:** testing requires actual participants and interpretation; do not treat a single opinion or passing automation as universal validation.

### FromSoftware: Elden Ring

**Documented:** Miyazaki describes accomplishment, freely paced adventure, customization, and reciprocal design between major bosses and their locations. Gameplay qualities help determine summon selection before additional characterization. [S5]

**Flavor inference:** overcoming a distinctive authored situation through personal preparation and exploration.

**Agent proposal:** define the challenge, what the player can learn or change, and how place and encounter reinforce each other. Do not reduce this approach to inflated damage or obscure instructions.

**Transfer risk:** multiple preparations and routes enlarge balancing work; one interview does not establish the entire studio's difficulty methodology.

### Larian: Divinity: Original Sin 2

**Documented:** Vincke's GDC deck covers pillars, situation reviews, feedback loops, cuts, interacting surfaces, and player tracking. Its closing lessons emphasize whiteboxing, iteration-ready processes, automation, real-world testing, and scope/documentation discipline. [S6]

**Flavor inference:** situations that accommodate player experimentation, supported by intensive iteration.

**Agent proposal:** start with a bounded situation and a few interacting rules; enumerate plausible attempted solutions and their consequences. Budget downstream implementation and test work before promising more options.

**Transfer risk:** agency generates combinations and authored consequences; a small team should not inherit the content obligations of a large RPG. The slides were inspected; the full recorded talk was not watched.

### Naughty Dog: The Last of Us

**Documented:** Its official podcast transcript connects emotional contrast with gameplay: brutality is balanced with warmth. Anthony Newman describes repetitive infected encounters prompting differentiation into multiple enemy classes during production. [S7]

**Flavor inference:** authored emotional pacing expressed through encounters as well as dialogue.

**Agent proposal:** define the emotional change a scene should produce, align interaction with it, and inspect pacing across scenes rather than judging each feature in isolation.

**Transfer risk:** performance, animation, and bespoke scenes are expensive. An intimate playable interaction may test an emotional idea more cheaply than cinematic production.

### Supergiant: Hades

**Documented:** Supergiant says Early Access shaped Hades from the outset, including modular structure and narrative. Repeated play exposes new combinations and story events; recurring characters remember interactions. [S8]

**Flavor inference:** repeated attempts renew both mechanical interest and character investment.

**Agent proposal:** ask what makes another attempt desirable beyond correcting an error. Prototype a short cycle with one meaningful variation or character consequence, not a full progression economy.

**Transfer risk:** event variety and continuity require content and state-management work. Repetition alone is not evidence of replay value.

## Implications for This Repository

These are our proposed adaptations, not procedures attributed verbatim to the studios:

1. **Taste and attraction before a solution.** Establish desired feelings, appealing situations, disliked experiences, and constraints. The user rejected salvage itself; do not continue rescuing that theme.
2. **Compare creative directions.** Offer three genuinely different player experiences, each with an immediate attraction, a defining interaction, a dominant design priority, an intentional sacrifice, and its largest uncertainty. Avoid three cosmetic versions of one mechanic.
3. **Choose a lead approach.** Select an experience-specific lens; use evidence-driven iteration as a shared discipline. Do not stack every studio's priorities into one design.
4. **Prototype the uncertain appeal.** Define what a person might enjoy discovering, performing, expressing, or feeling. A technically convenient deterministic example is not automatically a useful experience experiment.
5. **Separate understandability from desirability.** Observe an unassisted attempt first when evaluating onboarding. Later explanation can diagnose misunderstanding, but cannot retroactively count as unassisted comprehension.
6. **Stop without defensiveness.** Preserve negative feedback, classify the failed promise, and decide whether to clarify, revise the core, or abandon the direction before expanding documentation or content.

For the current prototype, the user's reports distinguish initial confusion, improved predictability after explanation/UI changes, an obvious sequence, and rejection of the theme. These are this user's actual reports, not a representative market study. The three-step prototype should remain a workflow/rule-validation artifact, not a presumed game direction.

An important correction to our earlier diagnosis: a unique solution is not by itself a defect. The question is whether discovering or executing it creates the intended experience. Multiple solutions are appropriate to some creative priorities, not a universal prerequisite for a good game. This is our design judgment, not a quoted studio rule.

## Proposed Next Deliverable

Revise the existing agent's concept-selection and evaluation behavior, subject to approval. Prefer concise reference material and changes to existing intake/gameplay/prototype/review guidance over six new personas or a large additional template system. A useful acceptance test is whether it can reject an unappealing, easily implemented concept and explain why competing directions might interest this user before producing another prototype.

No agent instructions, gameplay rules, or prototype files were changed by this research.

## Sources

- **S1:** British GQ, *The 100 greatest video games of all time, ranked by experts*. Page dated 2026-07-22; underlying poll explicitly 2023. `https://www.gq-magazine.co.uk/article/best-video-games-all-time`
- **S2:** BAFTA, *Shenmue Revealed as Most Influential Video Game of All Time, According to BAFTA Poll*, 2025-04-03. Public-vote press release; search-index text retrieved, direct fetch intermittently timed out. `https://www.bafta.org/media-centre/press-releases/most-influential-video-games-of-all-time-poll/`
- **S3:** Nintendo, *Ask the Developer Vol. 9, Tears of the Kingdom, Chapter 5*, Australian edition, 2023-05-12. Direct developer interview. `https://www.nintendo.com/au/news-and-articles/ask-the-developer-vol-9-the-legend-of-zelda-tears-of-the-kingdom-chapter-5/`
- **S4:** David Speyrer and Brian Jacobson, *Valve's Design Process for Creating Half-Life 2*. Deck in Valve's 2006 publication path; retrieved slides display a 2007 copyright. Process claims use slides 5-12 and 15-18, not a claim about today's organization. `https://cdn.fastly.steamstatic.com/apps/valve/2006/GDC2006_HL2DesignProcess.pdf`
- **S5:** Xbox Wire, direct Hidetaka Miyazaki interview, *From Software's Hidetaka Miyazaki on the Secrets of Elden Ring's Development*, 2022-05-27. `https://news.xbox.com/en-us/2022/05/27/from-softwares-hidetaka-miyazaki-on-the-secrets-of-elden-rings-development/`
- **S6:** Swen Vincke, *The Making of Divinity: Original Sin 2*, GDC 2019, 40-slide deck; closing lessons on PDF page 40. `https://media.gdcvault.com/gdc2019/presentations/Vincke_Swen_The_Making_of.pdf`
- **S7:** Naughty Dog, official *The Last of Us* podcast, episode 1 transcript; no publication date established from retrieved page. Anthony Newman section discusses emotional contrast and infected-enemy iteration. `https://www.naughtydog.com/podcasts/thelastofus/en/ep-01`
- **S8:** Supergiant Games, *Hades FAQ*, originally 2018-12-07; page states last updated 2025-07-16. Studio account, including Early Access and narrative design. `https://www.supergiantgames.com/blog/hades-faq/`
