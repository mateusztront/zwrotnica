document.addEventListener("DOMContentLoaded", function () {
    /**
     * HomePage - Help section
     */
    class Help {
        constructor($el) {
            this.$el = $el;
            this.$buttonsContainer = $el.querySelector(".help--buttons");
            this.$slidesContainers = $el.querySelectorAll(".help--slides");
            this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
            this.init();
        }

        init() {
            this.events();
        }

        events() {
            /**
             * Slide buttons
             */
            this.$buttonsContainer.addEventListener("click", e => {
                if (e.target.classList.contains("btn")) {
                    this.changeSlide(e);
                }
            });

            /**
             * Pagination buttons
             */
            this.$el.addEventListener("click", e => {
                if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
                    this.changePage(e);
                }
            });
        }

        changeSlide(e) {
            e.preventDefault();
            const $btn = e.target;

            // Buttons Active class change
            [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
            $btn.classList.add("active");

            // Current slide
            this.currentSlide = $btn.parentElement.dataset.id;

            // Slides active class change
            this.$slidesContainers.forEach(el => {
                el.classList.remove("active");

                if (el.dataset.id === this.currentSlide) {
                    el.classList.add("active");
                }
            });
        }

        /**
         * TODO: callback to page change event
         */
        changePage(e) {
            e.preventDefault();
            const page = e.target.dataset.page;

            console.log(page);
        }
    }

    const helpSection = document.querySelector(".help");
    if (helpSection !== null) {
        new Help(helpSection);
    }

    /**
     * Form Select
     */
    class FormSelect {
        constructor($el) {
            this.$el = $el;
            this.options = [...$el.children];
            this.init();
        }

        init() {
            this.createElements();
            this.addEvents();
            this.$el.parentElement.removeChild(this.$el);
        }

        createElements() {
            // Input for value
            this.valueInput = document.createElement("input");
            this.valueInput.type = "text";
            this.valueInput.name = this.$el.name;

            // Dropdown container
            this.dropdown = document.createElement("div");
            this.dropdown.classList.add("dropdown");

            // List container
            this.ul = document.createElement("ul");

            // All list options
            this.options.forEach((el, i) => {
                const li = document.createElement("li");
                li.dataset.value = el.value;
                li.innerText = el.innerText;

                if (i === 0) {
                    // First clickable option
                    this.current = document.createElement("div");
                    this.current.innerText = el.innerText;
                    this.dropdown.appendChild(this.current);
                    this.valueInput.value = el.value;
                    li.classList.add("selected");
                }

                this.ul.appendChild(li);
            });

            this.dropdown.appendChild(this.ul);
            this.dropdown.appendChild(this.valueInput);
            this.$el.parentElement.appendChild(this.dropdown);
        }

        addEvents() {
            this.dropdown.addEventListener("click", e => {
                const target = e.target;
                this.dropdown.classList.toggle("selecting");

                // Save new value only when clicked on li
                if (target.tagName === "LI") {
                    this.valueInput.value = target.dataset.value;
                    this.current.innerText = target.innerText;
                }
            });
        }
    }

    document.querySelectorAll(".form-group--dropdown select").forEach(el => {
        new FormSelect(el);
    });

    /**
     * Hide elements when clicked on document
     */
    document.addEventListener("click", function (e) {
        const target = e.target;
        const tagName = target.tagName;

        if (target.classList.contains("dropdown")) return false;

        if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
            return false;
        }

        if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
            return false;
        }

        document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
            el.classList.remove("selecting");
        });
    });

    /**
     * Switching between form steps
     */
    class FormSteps {
        constructor(form) {
            this.$form = form;
            this.$next = form.querySelectorAll(".next-step");
            this.$prev = form.querySelectorAll(".prev-step");
            this.$step = form.querySelector(".form--steps-counter span");
            this.currentStep = 1;

            this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
            const $stepForms = form.querySelectorAll("form > div");
            this.slides = [...this.$stepInstructions, ...$stepForms];

            this.init();
        }

        /**
         * Init all methods
         */
        init() {
            this.events();
            this.updateForm();
        }

        /**
         * All events that are happening in form
         */
        events() {
            // Next step
            this.$next.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep++;
                    this.updateForm();
                });
            });

            // Previous step
            this.$prev.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep--;
                    this.updateForm();
                });
            });

            // Form submit
            this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
        }

        /**
         * Update form front-end
         * Show next or previous section etc.
         */
        updateForm() {
            this.$step.innerText = this.currentStep;

            // TODO: Validation

            this.slides.forEach(slide => {
                slide.classList.remove("active");

                if (slide.dataset.step == this.currentStep) {
                    slide.classList.add("active");
                }
            });

            this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
            this.$step.parentElement.hidden = this.currentStep >= 6;

            // TODO: get data from inputs and show them in summary
            //playground start

            // let inputCategories = this.$form.querySelectorAll("input[name=categories]:checked");
            // console.log(inputCategories)

            // fetch miedzy krokami 2 i 3 z id kategorii, if i wstrzykiwac HTML dla kazdego

            //playground end
            //data gathering
            // var elements = document.forms[0].elements;
            let elements = this.$form.querySelector("form").elements;
            document.querySelector("#bags").innerHTML = elements.namedItem("bags").value;
            document.querySelector("#fundation-name").innerHTML = elements.namedItem("organization").value;
            document.querySelector("#address").innerHTML = elements.namedItem("address").value;
            document.querySelector("#city").innerHTML = elements.namedItem("city").value;
            document.querySelector("#postcode").innerHTML = elements.namedItem("postcode").value;
            document.querySelector("#phone").innerHTML = elements.namedItem("phone").value;
            document.querySelector("#donation_date").innerHTML = elements.namedItem("data").value;
            document.querySelector("#donation_time").innerHTML = elements.namedItem("time").value;
            document.querySelector("#more_info").innerHTML = elements.namedItem("more_info").value;
        }

        /**
         * Submit form
         *
         * TODO: validation, send data to server
         */

        submit(e) {
            e.preventDefault();

            var dataForm = new FormData();

            //   for (var i = 0; i < this.$form.length; ++i) {
            //     dataForm.append(this.$form[i].name, this.$form[i].value);
            // }
            let elements = this.$form.querySelector("form").elements;
            dataForm.append("bags", elements.namedItem("bags").value);
            dataForm.append("organization", elements.namedItem("organization").value);
            dataForm.append("address", elements.namedItem("address").value);
            dataForm.append("city", elements.namedItem("city").value);
            dataForm.append("postcode", elements.namedItem("postcode").value);
            dataForm.append("phone", elements.namedItem("phone").value);
            dataForm.append("data", elements.namedItem("data").value);
            dataForm.append("time", elements.namedItem("time").value);
            dataForm.append("more-info", elements.namedItem("more_info").value);

            console.log(dataForm);
            // JavaScript function to get cookie by name; retrieved from https://docs.djangoproject.com/en/3.1/ref/csrf/
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

// JavaScript wrapper function to send HTTP requests using Django's "X-CSRFToken" request header
            function sendHttpAsync(path, method, body) {

                let props = {
                    method: method,
                    headers: {
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                    mode: "same-origin",
                }
props.body = body
                // if (body !== null && body !== undefined) {
                //     props.body = JSON.stringify(body);
                // }

                return fetch(path, props)
                    .then(response => {
                        return response.json()
                            .then(result => {
                                return {
                                    ok: response.ok,
                                    body: result
                                }
                            });
                    })
                    .then(resultObj => {
                        return resultObj;
                    })
                    .catch(error => {
                        throw error;
                    });
            }


            // fetch('/add_donation/', {
            //     method: 'POST',
            //     headers:{'X-CSRFToken':getCookie("csrftoken")},
            //     body: dataForm,
            //     credentials: 'include',
            // })
            //     .then(response => response.json())
            //     .then(data => {
            //         console.log('Success:', data);
            //     })
            //     .catch(error => {
            //         console.log('Error:', error);
            //     });
            // this.currentStep++;
            // this.updateForm();
            sendHttpAsync("", "post", dataForm)
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                });
        }
    }

    const form = document.querySelector(".form--steps");
    if (form !== null) {
        new FormSteps(form);
    }
});
