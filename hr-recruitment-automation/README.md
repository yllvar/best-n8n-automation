# AI-Driven HR Automation & Chatbot Templates for n8n

## Surviving the Modern HR Nightmare

Right, the job market. Currently, it's an absolute disaster. For every decent position, there are 500 applicants—half of whom are bots, a quarter are wildly unqualified, and most of the rest are responding to job posts from scammer recruiters who don't even work for real companies. Meanwhile, HR departments are drowning in CVs, recruiters are lying about "exciting opportunities" that pay £25k for senior roles, and the entire system is fundamentally broken.

But what if you could cut through the nonsense? What if AI could filter the 500 bot applications down to the 10 actual candidates? What if automation could spot the scammer recruiters before they waste your time? What if HR could actually function in an oversupplied job market without losing their minds?

Well, now it can.

This repository contains what is possibly the most advanced collection of HR automation templates... *in the world.* These aren't just recruitment tools. These are survival systems for navigating a job market where supply vastly exceeds demand, scammers outnumber legitimate recruiters, and everyone's CV is enhanced by ChatGPT anyway.

Some say these workflows can replace entire HR departments. Some say they're the only way to survive modern recruitment. All we know is... they work brilliantly in conditions that would break traditional hiring processes.

---

## The Templates: Your HR Survival Kit

### 1. HR Job Posting and Evaluation with AI: The Scam-Proof Hiring Pipeline

Job posting in 2025. You post one opening. 500 applications arrive. 200 are bot-submitted. 150 are from people who didn't read the description. 100 are wildly unqualified. 50 might be legitimate. Good luck finding them manually.

**What it does:**
- **Custom job application forms** - with CV upload (filtering bots at the gate)
- **Airtable integration** - applicant tracking that actually tracks applicants
- **AI-powered CV matching** - scoring candidates against actual job requirements, not just keyword density
- **Multi-stage evaluation** - application, phone screen, onsite interview (systematic filtering)
- **Automated notifications** - keeping humans informed without manual email sending

**Why This Matters:** The AI reads every CV (humans can't). Scores every candidate (consistently, without bias or fatigue). Filters the noise (bot applications don't pass AI screening). What remains are actual candidates worth interviewing.

**The Job Market Reality:** With oversupply, you can't manually review 500 CVs. But you also can't miss the 5 actually qualified candidates buried in the pile. This finds them automatically. That's not convenience. That's survival.

**Scammer Detection:** When a "recruitment agency" posts fake jobs to harvest CVs, this workflow spots the patterns—vague requirements, unrealistic salary ranges, generic descriptions. The AI knows what real job posts look like because it's seen thousands of them.

---

### 2. HR & IT Helpdesk Chatbot with Audio Transcription: The Policy Oracle

HR helpdesks. Traditionally, humans answering the same questions repeatedly. "What's the leave policy?" "How do I claim expenses?" "Is this IT issue covered?" Asked 47 times daily. HR staff slowly lose the will to live.

**What it does:**
- **PDF document ingestion** - company policies become queryable knowledge
- **Audio transcription** - voice queries supported (because typing is too much effort)
- **Vector search** - context-aware responses, not keyword matching
- **Telegram integration** - chat interface that actually works
- **OpenAI-powered intelligence** - understanding questions, not just scanning for keywords

**The Experience:** Employee asks "Can I take leave during December?" The bot checks your leave policy PDF, understands the context, provides accurate answer with policy citation. No HR staff interrupted. No waiting. Just answers.

**Why This Works in Oversupplied Markets:** When you have more staff (because hiring is cheap in oversupplied markets), you get more HR queries. This scales support without scaling HR headcount. That's efficiency in conditions that traditionally create overhead.

---

### 3. CV Screening with OpenAI: The Bot-Application Filter

CV screening in 2025. Half the applications are AI-generated. A quarter are from bots. Most are copy-pasted spam. Finding real candidates requires reading hundreds of CVs that all claim "passionate team player with excellent communication skills."

**What it does:**
- **Automated CV download** - PDF/DOC parsing without human clicking
- **Job description matching** - sending CV + requirements to OpenAI for analysis
- **Matching score generation** - quantitative assessment, not gut feelings
- **Candidate summarization** - key qualifications extracted, not buried in fluff
- **Supabase storage** - structured data for actual analysis

**The Filtering Power:** AI spots patterns humans miss. Bot-generated CVs have tells. Mass-applied applications show inconsistencies. ChatGPT-enhanced resumes use predictable phrases. The AI knows what real experience looks like versus what generated content sounds like.

**Scammer Recruiter Defense:** When scammer recruiters submit candidates they don't actually represent (harvesting your job details to repost elsewhere), this workflow checks consistency—does the CV match the claimed experience? Do the contact details check out? Are there red flags in the submission pattern?

**Market Oversupply Advantage:** With 500 applications, human screening misses qualified candidates due to fatigue. AI screening doesn't get tired. Doesn't get biased. Doesn't miss the diamond in application #347 because it's been a long day.

---

### 4. BambooHR AI-Powered Company Policies and Benefits Chatbot: The Employee Self-Service Revolution

Employee queries. Benefits questions. Policy clarifications. Traditionally requires HR staff availability, policy knowledge, and patience to answer the same questions 17 times daily.

**What it does:**
- **BambooHR integration** - real-time employee and policy data (not outdated PDFs)
- **OpenAI + vector search** - accurate, context-aware responses (understands questions, not just keywords)
- **Employee lookup** - department-based queries supported (understanding organizational context)
- **Multiple document types** - policies, benefits, procedures all queryable
- **24/7 availability** - because HR queries don't respect business hours

**Why This Matters:** Employees get instant answers. HR doesn't get interrupted. Policies are applied consistently. Benefits are explained clearly. It's HR support that scales infinitely without hiring more HR staff.

**The Oversupply Context:** When you have more employees (because hiring is cheap), you get exponentially more HR queries. Traditional HR can't scale to match. This chatbot can. That's the difference between drowning and swimming.

---

## Getting Started: Deployment in the Chaos

Right, here's how you actually deploy these in the current nightmare job market:

**1. Import Workflows**
   - Download JSON files
   - Import into n8n
   - Choose templates that address your specific pain points

**2. Configure Credentials**
   - **OpenAI** - the AI that actually understands context (expensive but worth it)
   - **Airtable** - applicant tracking without enterprise CRM costs
   - **Supabase** - structured data storage that scales
   - **BambooHR** - if you're using it (Template 4 only)
   - **Telegram** - if supporting chat interfaces

**3. Adjust Settings**
   - **Form fields** - capture information you actually need
   - **Document sources** - point to your actual policy documents
   - **Notification rules** - alert humans when humans are needed
   - **Scoring thresholds** - define what "qualified" means for your roles

**4. Deploy and Test**
   - **Test with known-good CVs** - ensure AI scoring makes sense
   - **Test with known-bad applications** - ensure filtering works
   - **Test with real queries** - ensure chatbot responses are accurate
   - **Then go live** - cautiously, monitoring results

**Critical Warning:** These templates filter aggressively because the modern job market requires aggressive filtering. If you're getting zero qualified candidates, your job posting might be the problem (unrealistic requirements, scammer-adjacent language, below-market compensation). The AI can't fix a fundamentally broken job posting.

---

## Why Use These Templates? The Survival Argument

**Save Time:**
- Don't manually review 500 bot applications
- Don't answer the same HR questions 47 times daily
- Don't waste hours on scammer recruiter submissions

**Improve Accuracy:**
- AI doesn't get tired after CV #200
- Consistent evaluation criteria applied to all candidates
- Pattern recognition spots bots and scammers humans miss

**Enhance Experience:**
- Real candidates get faster responses (not buried under bot applications)
- Employees get instant answers (not waiting on HR availability)
- Everyone wastes less time on broken processes

**Survive Oversupply:**
- When supply exceeds demand, volume becomes unmanageable
- Traditional HR processes break at scale
- These automations scale infinitely without additional headcount

**The Reality:** Without automation, modern recruitment is unmanageable. With automation, it's merely difficult. That's not hyperbole. That's the current state of the job market.

---

## The Job Market Context Nobody Wants to Discuss

Let's be brutally honest about what's happening:

**The Oversupply Problem:**
- 500+ applications per decent role
- Most applicants are desperate, not qualified
- Everyone uses ChatGPT to enhance CVs
- Distinguishing real talent from enhanced mediocrity requires AI

**The Scammer Epidemic:**
- Fake recruiters posting fake jobs to harvest CVs
- Real recruiters lying about compensation and role details
- Companies posting jobs they're not actually filling (market research, compliance theater)
- Applicants lying about experience because everyone else is lying

**The Traditional HR Collapse:**
- Manual CV screening: impossible at 500+ applications
- Phone screens: can't call 500 people
- Interview scheduling: overwhelmed by volume
- Offer negotiations: ghosting is standard because oversupply means disposable candidates

**These Templates Address:**
- **Volume** - AI processes 500 CVs without fatigue
- **Scams** - pattern recognition spots fake submissions
- **Consistency** - evaluation criteria applied uniformly
- **Scale** - grows with application volume without hiring more HR

**The Uncomfortable Truth:** The job market is broken. Traditional hiring processes don't work anymore. You either automate or drown. There's no middle ground.

---

## License: The Legal Formality

MIT License.

**Translation:** Use it. Modify it. Deploy it. Build businesses on it. We're not responsible if it filters out your perfect candidate because you configured it wrong. Read the instructions. Test thoroughly. Then deploy.

---

## And on that bombshell...

You now have four HR automation templates designed for a job market where oversupply meets widespread scamming meets AI-enhanced applications. Some say automation dehumanizes hiring. Some say the job market was dehumanized long before AI arrived. All we know is... these templates help you survive conditions that would otherwise be unmanageable.

**HR automation for a broken job market—filtering the noise so you can find the signal!**

*"The job market is broken. These templates don't fix it. They just help you survive it."*

**Some say these workflows can process more applications in an hour than an HR team can in a week. All we know is... they're called the Recruitment Stig.**

Now go forth and automate your hiring. The alternative is drowning in 500 applications where 450 are noise and finding the 50 legitimate candidates requires superhuman effort you don't have.

*P.S. - If you're an applicant reading this and thinking "this is why I never get responses," you're probably right. But you're also competing with 499 other applicants, half of whom are bots. The system is broken for everyone. These templates just help employers survive the same chaos you're experiencing from the other side.*