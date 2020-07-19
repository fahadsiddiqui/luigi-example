import time

import luigi


class Foo(luigi.WrapperTask):
    task_namespace = 'examples'

    def run(self):
        print("Running Foo")

    def requires(self):
        for i in range(10):
            yield Bar(i)


class Bar(luigi.Task):
    task_namespace = 'examples'
    num = luigi.IntParameter()

    def run(self):
        time.sleep(1)
        self.output().open('w').close()

    def output(self):
        """
        Returns the target output for this task.
        :return: the target output for this task.
        :rtype: object (:py:class:`~luigi.target.Target`)
        """
        time.sleep(1)
        return luigi.LocalTarget('/tmp/bar/%d' % self.num)