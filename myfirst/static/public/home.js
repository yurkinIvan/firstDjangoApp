window.onload = function() {
    
    const 
        slider	    = document.querySelector(".slider"),
        scrollbar   = document.querySelector(".scrollbar"),
        scrollWrapp = document.querySelector(".scrollbar-wrapper"), 
        container   = document.querySelector(".articles"),
        loadBtn     = document.querySelector(".load-btn");

    let articlesLoaded = 5;

    /***************************** SLIDER *****************************/
    
    // TODO: Create scroll article image
    slider.onmousedown = function(e) {

        const coords	      = getCoords(this);
        const shiftX    	  = e.pageX - coords.left;
        const scrollbarCoords = getCoords(scrollbar);

        document.onmousemove = function(e) {
    
            let newLeft = e.pageX - scrollbarCoords.left - shiftX;
    
            if (newLeft < "0") {
                newLeft = "0"
            };
    
            if (newLeft > scrollbar.offsetWidth - slider.offsetWidth) {
                newLeft = scrollbar.offsetWidth - slider.offsetWidth;
            }
    
            let left          = parseFloat(slider.style.left); // Moving the slider in px
            let scrollPercent = (left * 100)/(scrollbar.offsetWidth - slider.offsetWidth); // Moving the slider in %
            let index		  = ((container.scrollWidth - container.offsetWidth)*scrollPercent)/100; // Moving the container in px
    
            container.style.transform = `translateX(-${index}px)`;
            slider.style.left = `${newLeft}px`;
    
            document.onselectstart = function() {
                return false;
            };
    
        }
    
        document.onmouseup = function () {
            document.onmousemove = slider.onmouseup = null;
            document.onselectstart = function() {
                return true;
            };
        }
    }
    
    slider.ondragstart = function () {
        return false;
    }

    /***************************** LOAD ARTICLES *****************************/

    loadBtn.onclick = (e) => {
        getArticles();
    }
    
    /**
     * Get element's coordinates
     * @param {Object} elem event object of element
     */
    function getCoords(elem) {
        let coords = elem.getBoundingClientRect();
        return {
            left: coords.left + pageXOffset,
            top: coords.top + pageYOffset
        };
    }

    /**
     * Get ten articles from DB and increases count of articles
     */
    function getArticles() {
        
        fetch(`/loadArticles?count=${articlesLoaded}`, {method: "GET"})
            .then(res => res.json())
            .then(articles => {
                if (articles.length == 0) {
                    showMessage('Статей больше нет');
                } else {
                    console.log(articles)
                    articlesLoaded += articles.length;
                    createArticles(articles);
                    jumpSlider();
                }
            })
            .catch((e) => {
                showMessage('Произошла ошибка');
            });

    }

    /**
     * Create article's card
     * @param {Array} articles array with 10 articles
     */
    function createArticles(articles) {
        
        for (let i = 0; i < articles.length; i++) {

            let
                title 	= articles[i].title,
                url   	= articles[i].img,
                text  	= articles[i].text,
                created = articles[i].date;

            let
                card 	  = document.createElement(`div`),
                imgWrapp  = document.createElement(`div`),
                cardBody  = document.createElement(`div`),
                line      = document.createElement(`div`),
                cardTitle = document.createElement(`a`),
                cardText  = document.createElement(`p`),
                date 	  = document.createElement(`span`),
                img		  = document.createElement(`img`);

            card.classList.add(`card`);
            imgWrapp.classList.add(`card__img`);
            cardBody.classList.add(`card__body`);
            line.classList.add(`separator`);
            cardTitle.classList.add(`title`);
            cardText.classList.add(`article-text`);
            date.classList.add(`date`),
            
            container.insertBefore(card, loadBtn)
            card     .appendChild(imgWrapp);
            imgWrapp .appendChild(img);
            card     .appendChild(cardBody);
            cardBody .appendChild(cardTitle);
            cardBody .appendChild(cardText);
            cardBody .appendChild(line);
            cardBody .appendChild(date);

            img.src   			  = url;
            cardTitle.textContent = title;
            cardTitle.href = articles[i].id;
            cardText.textContent  = articles[i].desc;
            date.textContent      = created;

        }

    }

    function showMessage(message) {
        error = document.createElement(`p`);
        error.classList.add("error-message");
        error.textContent = message;

        container.lastElementChild.remove(); // Delete load-btn
        container.appendChild(error);
    }

    function jumpSlider() {

        let containerLeft = -(getCoords(container).left - 25);
    
        let percents = (containerLeft*100)/(container.scrollWidth);
        let px = (percents*scrollbar.offsetWidth)/100;
        
        slider.style.left = `${px}px`;
    
    };
    

}