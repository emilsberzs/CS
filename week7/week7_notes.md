# Application security principles: testing and debugging. (part 1)
## Application security(AppSec)
- Protecting apps from security flaws
- Tools, processes and best practices used during design, development, deployment and maintenance
- Applies to web, mobile, desktop and cloud
- Must be considered through full SDLC
### Security concepts for developers
- Least privilege
- Input validation
- Secure defaults
- Defence in depth (multiple security layers)
- Fail securely
### Security threats during app development
- Poor input validation
- Exposed debug code
- Weak authentication
- Insecure APIs
- Lack of access control
- No security testing
### Open Worldwide Application Security Project (OWASP) 
- Non-profit community
- Creates resources for secure development
- OWASP Top 10 2021:
    1. Broken access control
    2. Cryptographic failures
    3. Injection
    4. Insecure design
    5. Security misconfiguration
    6. Vulnerable and outdated components
    7. Identification and Authentication failures
    8. Software and data integrity failures
    9. Security logging and monitoring failures
    10. Server-side request forgery

## Secure coding 
- Writing code that avoids security flaws
- Prevents vulnerabilities from the start
- Resilient to mis-use and attacks
- Insecure code can lead to:
    - Data breaches
    - Account takeovers
    - Malware injection
    - Legal/Compliance failures
    - System downtime
### Core principles of secure coding
- Security by design
- Least privilege
- Input validation
- Output Encoding
- Fail securely
- Avoid hiding security details
- Keep it simple
### Best practices in secure coding
- Developers should:
    - Validate and sanitize all input
    - Use prepared statements for queries
    - Implement proper authentication
    - Avoid hardcoded credentials
    - Choose secure libraries
    - Handle errors safely
    - Review and test code for security
### Roles in producing secure code
- Developers:
    - Write clean, secure code
- Team leads:
    - Promote best practices
- Testers:
    - Identify issues
- Architects:
    - Design safe systems
- DevOps:
    - Secure the environment
- Security teams:
    - Provide guidance 

### Secure coding in SDLC
- Requirements:
    - Define security goals
- Design:
    - Apply secure architecture
- Development:
    - Follow secure coding practices
- Testing:
    - Include securty tests
- Deployment:
    - Lock down configurations
- Maintenance:
    - Monitor and patch
### Failure examples from industry
- Social media breach due to hardcoded administrator password
- Healthcare app exposed patient data
- Online store experienced customer card data theft
- Government site went down because of unhandled errors 

## Secure file handling and configuration
-