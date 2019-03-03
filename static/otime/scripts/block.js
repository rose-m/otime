(function () {
    /*
        We use an IIFE to properly encapsulate all JavaScript code and prevent
        leaking anything into global scope.
     */
    var answersInput = jQuery('#timepref__answers');
    if (!answersInput.length) {
        throw new Error('cannot find answers input #timepref__answers');
    }

    // Block index and state are read from existing DOM elements
    var blockIndex = parseInt(answersInput.attr('data-block-index')) - 1;
    var state = JSON.parse(answersInput.val() || '[]');

    jQuery('.timepref__question-choices').each(function () {
        /*
            We parse every existing choice row and register proper listeners to handle user selection
            of choices.
         */
        var choiceRow = jQuery(this);
        var questionIndex = parseInt(choiceRow.attr('data-question-index'));
        var questionRow = jQuery('.timepref__question-index-' + questionIndex);
        var valueWidth = jQuery('.timepref__question-start td.text-center').first().width();

        choiceRow.find('.timepref__question-choice').on('click', function (e) {
            if (jQuery(e.target).is('input')) {
                return;
            }
            jQuery(this).find('input').click();
        });

        choiceRow.find('input[type=radio]').on('change', function () {
            choiceRow
                .find('.timepref__question-choice-selected')
                .removeClass('timepref__question-choice-selected');
            if (choiceRow.find('input:checked').length) {
                questionRow.removeClass('timepref__question-unanswered');
                choiceRow.find('input:checked')
                    .closest('.timepref__question-choice')
                    .addClass('timepref__question-choice-selected');
            } else {
                questionRow.addClass('timepref__question-unanswered');
            }
            checkAllQuestions();
            updateState();
        });

        choiceRow.find('input[type="range"]').each(function () {
            var rangeInput = jQuery(this);
            var rangeTd = rangeInput.closest('td');

            rangeTd.css({
                paddingLeft: valueWidth / 2,
                paddingRight: valueWidth / 2
            });

            rangeInput.rangeslider({
                polyfill: false,
                onSlideEnd: function () {
                    checkAllQuestions();
                    updateState();
                }
            });
        });
    });

    checkAllQuestions();
    updateState();

    /**
     * Serializes the current user selection and updates the current state of Block answers
     */
    function updateState() {
        var blockState = [];
        jQuery('.timepref__question-choices').each(function () {
            var choiceRow = jQuery(this);
            var selected = choiceRow.find('input:checked');
            if (selected.length) {
                blockState.push(parseInt(selected.val()));
            } else {
                var range = choiceRow.find('input[type=range]');
                if (range.length) {
                    blockState.push(parseInt(range.val()));
                } else {
                    blockState.push(-1);
                }
            }
        });
        state[blockIndex] = blockState;
        answersInput.val(JSON.stringify(state));
    }

    /**
     * Checks whether all questions have yet been answered by the user, i.e. a choice has been selected
     */
    function checkAllQuestions() {
        if (jQuery('.timepref__question-unanswered').length) {
            jQuery('.timepref__next-button').hide();
            jQuery('.timepref__waiting').show();
        } else {
            jQuery('.timepref__next-button').show();
            jQuery('.timepref__waiting').hide();
        }
    }
}());
