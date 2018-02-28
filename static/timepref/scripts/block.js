(function () {
    var answersInput = jQuery('#timepref__answers');
    if (!answersInput.length) {
        throw new Error('cannot find answers input #timepref__answers')
    }
    var blockIndex = parseInt(answersInput.attr('data-block-index')) - 1;
    var state = JSON.parse(answersInput.val() || '[]');

    jQuery('.timepref__question-choices').each(function () {
        var choiceRow = jQuery(this);
        var questionIndex = parseInt(choiceRow.attr('data-question-index'));
        var questionRow = jQuery('.timepref__question-index-' + questionIndex);

        choiceRow.find('.timepref__question-choice').on('click', function (e) {
            if (jQuery(e.target).is('input')) {
                return;
            }
            jQuery(this).find('input').click();
        });

        choiceRow.find('input').on('change', function () {
            if (choiceRow.find('input:checked').length) {
                questionRow.removeClass('timepref__question-unanswered');
            } else {
                questionRow.addClass('timepref__question-unanswered');
            }
            checkAllQuestions();
            updateState();
        });
    });

    function updateState() {
        var blockState = [];
        jQuery('.timepref__question-choices').each(function () {
            var choiceRow = jQuery(this);
            var selected = choiceRow.find('input:checked');
            blockState.push(selected.length ? parseInt(selected.val()) : -1);
        });
        state[blockIndex] = blockState;
        answersInput.val(JSON.stringify(state));
    }

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
