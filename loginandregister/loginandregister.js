let PRICEALPHA_loginRegisterClick = document.querySelector(".PRICEALPHA_loginRegister");
let indexbody = document.getElementById("indexbody");

PRICEALPHA_loginRegisterClick.addEventListener("click", () => {
    console.log("Button Action");

    let Logincontainer = document.createElement("div");
    Logincontainer.classList.add("loginandregisterContainer");
    indexbody.appendChild(Logincontainer);


     // ********** Close Button **********
     let closeButton = document.createElement("button");
     closeButton.classList.add("closeButton");
     closeButton.textContent = "X"; // Close symbol
     Logincontainer.appendChild(closeButton);
 
     closeButton.addEventListener("click", () => {
         // Remove the container from the DOM
         Logincontainer.remove();
     });

    //************main body login */
    let loginbody = document.createElement("div");
    loginbody.classList.add("loginbody");
    Logincontainer.appendChild(loginbody);

    //************left */
    let loginbodyleft = document.createElement("div");
    loginbodyleft.classList.add("loginbodyleft");
    loginbody.appendChild(loginbodyleft);

    let loginbodyleftthe2 = document.createElement("h1");
    loginbodyleftthe2.classList.add("loginbodyleftthe2");
    loginbodyleftthe2.textContent = "Try to more Grow.";
    loginbodyleft.appendChild(loginbodyleftthe2);

    //************right */
    let loginbodyRight = document.createElement("div");
    loginbodyRight.classList.add("loginbodyRight");
    loginbody.appendChild(loginbodyRight);

    let loginbodyRighth1 = document.createElement("h2");
    loginbodyRighth1.classList.add("loginbodyRighth1");
    loginbodyRighth1.textContent = "Welcome To Price Alpha";
    loginbodyRight.appendChild(loginbodyRighth1);

    //*********Download PDF Section */
    let downloadContainer = document.createElement("div");
    downloadContainer.classList.add("downloadContainer");
    loginbodyRight.appendChild(downloadContainer);

    let downloadText = document.createElement("p");
    downloadText.classList.add("downloadText");
    downloadText.textContent = "Download PDF for Learing:";
    downloadContainer.appendChild(downloadText);

    // Create buttons for each PDF option
    let pdfOptions = [
        { name: "Beginner's Guide [English]", file: "docs/Chart Petterns Book English_022258.pdf" },
        { name: "Beginner's Guide [Hindi]", file: "docs/Chart Patten Book hindi_022246.pdf" },
        { name: "Candledtick Analysis [English]", file: "docs/Candlelstick Patten English_022219.pdf" },
        { name: "Candledtick Analysis [Hindi]", file: "docs/Candlelstick Patten Bookhindi_022236.pdf" },
        { name: "Tips", file: "docs/tips.pdf" }, // Fifth option
    ];

    pdfOptions.forEach(option => {
        let downloadButton = document.createElement("button");
        downloadButton.classList.add("downloadButton");
        downloadButton.textContent = option.name;
        downloadContainer.appendChild(downloadButton);

        // Add event listener for each button
        downloadButton.addEventListener("click", () => {
            const link = document.createElement("a");
            link.href = option.file; // Path to the corresponding PDF
            link.download = option.name + ".pdf"; // Default filename
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    });
});
