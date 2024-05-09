# components/slip_form.py
import React, { useState } from 'react';
import { Form, Formik } from 'formik';
import { TextField, Button } from '@material-ui/core';
import * as Yup from 'yup';

const SlipFormSchema = Yup.object().shape({
  title: Yup.string().required('Title is required'),
  description: Yup.string().required('Description is required'),
});

interface SlipFormProps {
  onSubmit: (values: { title: string; description: string }) => void;
  initialValues?: { title: string; description: string };
}

const SlipForm: React.FC<SlipFormProps> = ({ onSubmit,initialValues }) => {
  return (
    <Formik
      initialValues={initialValues || { title: '', description: '' }}
      validationSchema={SlipFormSchema}
      onSubmit={onSubmit}
    >
      {({ values, handleChange, handleSubmit }) => (
        <Form onSubmit={handleSubmit}>
          <TextField
            name="title"
            label="Title"
            value={values.title}
            onChange={handleChange}
            fullWidth
            margin="normal"
          />
          <TextField
            name="description"
            label="Description"
            value={values.description}
            onChange={handleChange}
            fullWidth
            multiline
            rows={4}
            margin="normal"
          />
          <Button type="submit" variant="contained" color="primary">
            Submit
          </Button>
        </Form>
      )}
    </Formik>
  );
};

export default SlipForm;
